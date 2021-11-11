from rest_framework import serializers
from .models        import PQR, PersonaSoporte

class PersonaSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaSoporte
        fields = '__all__'

class PQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQR

        # lo que le enviamos a la db por medio de la db
        # o
        # lo que le enviamos a la vista
        fields = ['persona_soporte', 'estado', 'comentario']