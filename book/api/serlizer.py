from urllib import request

from django.contrib.postgres import serializers
from rest_framework import serializers
from catagory.models import *

class CatgorySerlixer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields=['id','name']
class BookSerlizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=10)
    create_date = serializers.DateField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)
    image = serializers.ImageField( required=False,allow_null=True)
    Catagory = serializers.PrimaryKeyRelatedField(
        queryset=Catagory.objects.all(),
       )
    is_active = serializers.BooleanField(default=True)

    #private logic to insert
    # def create(self,validated_data):
    #     pass
