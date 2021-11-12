from rest_framework import serializers
from .models        import PQR, PersonaSoporte, Bank
from django.contrib.auth.models import User

class PersonaSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaSoporte
        fields = '__all__'

class PQRSerializer(serializers.ModelSerializer):

    persona_soporte : PersonaSoporteSerializer(read_only=True)
        #Sobreescribimos este parametro, para no mostrar el id foraneo, si no todo el objeto de la persona
        #read_only -> solo para lectura

    class Meta:
        model = PQR

        # lo que le enviamos a la db por medio de la db
        # o
        # lo que le enviamos a la vista
        fields = ['persona_soporte', 'estado', 'comentario']


# User viene directamente  de Django
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

# serializer muchos a muchos
class BankSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    # (many=True -> trae muchos usuarios para cada banco)

    class Meta:
        model = Bank
        fields = ['users', 'name']