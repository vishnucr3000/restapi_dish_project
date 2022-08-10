from rest_framework import serializers
from dishes.models import Dishes
from django.contrib.auth.models import User

class DishesSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    category=serializers.CharField()
    rating=serializers.FloatField()

    def validate(self, attrs):
        price=attrs.get("price")
        name=attrs.get("name")
        if price<0 or len(name)<3:
            raise serializers.ValidationError("Invalid Price or name")
        else:
            return attrs

class DishesModelSerializer(serializers.ModelSerializer):
    class Meta():

        model=Dishes
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password"
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)