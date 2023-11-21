#importamos de la libreria de DRF la clase serializares
from rest_framework import serializers
from .models import Libro

#class LibroSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=255)
    # genre = serializers.CharField(max_length=255)
    # year = serializers.CharField(max_length=255)
    # author = serializers.CharField(max_length=255)
    # create_at = serializers.DateTimeField(read_only=True)
    # update_at = serializers.DateTimeField(read_only=True)


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = "__all__"

        read_only_fields = ("id","created_at","updated_at")



