# views


from django.shortcuts   import render
from rest_framework     import generics 
from .serializer        import PQRSerializer, PersonaSoporteSerializer
from .models            import PersonaSoporte, PQR

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