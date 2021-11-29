# views


from django.shortcuts   import render
from rest_framework     import generics, views, authentication, permissions, status
from .serializer        import PQRSerializer, PersonaSoporteSerializer, BankSerializer, UserSerializer, UserCreationSerializer
from .models            import PersonaSoporte, PQR, Bank
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

#   ListCreateAPIView -> nos proporciona endpoitns para leer y crear
#   ListCreateAPIView -> nos proporciona endpoitns para actualizar y eliminar

class PersonaSoporteListCreate(generics.ListCreateAPIView):
    queryset = PersonaSoporte.objects.all()  #conjunto de datos a usar
                #PersonaSoporte.objects     -> llamamos al ORM de PersonaSoporte
                #.all()                     -> llamamos todos los datos

    serializer_class = PersonaSoporteSerializer     #traemos los serializer

class PersonaSoporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonaSoporte.objects.all()

    serializer_class = PersonaSoporteSerializer 


class PQRListCreate(generics.ListCreateAPIView):
    queryset = PQR.objects.all()

    serializer_class = PQRSerializer

class PQRUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PQR.objects.all()

    serializer_class = PQRSerializer

# vistas banco muchos a muchos
class BankListCreate(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankUpdateDelete(generics.RetrieveUpdateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer



#Configs para recibir token - APIGateway
class UserRetrieve(views.APIView):
    # autenticacion por token
    authentication_classes = [authentication.TokenAuthentication]
    #la persona tiene que estar autenticada
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)   #request.user -> usuario de ese token
                                                    # lo serializamos con UserSerializer
        return Response(data=serializer.data, status=status.HTTP_200_OK)

        #se agrega a las urls


# creamos User manual, con el fin de guardar toda la info, de la relacion uno a uno en PersonaSoporte
class UserCreate(views.APIView):
    def post(self, request):
        #serializamos lo que llega en la peticion
        serializer = UserCreationSerializer(data=request.data)

        #validamos si es correcto(que no exista, contras correctas,etc)
        if serializer.is_valid():
            #llamamos al ORM de User
            #con create_user creamos objetos manuales en la DB
            user = User.objects.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            #creamos una persona soporte, y le enviamos el objeto con la info extra
            # en este caso solo utilizamos el campo extra edad
            PersonaSoporte.objects.create(user=user, edad=request.data['edad'])
            return Response(status=status.HTTP_201_CREATED)
