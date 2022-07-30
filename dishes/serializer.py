from rest_framework import serializers

class DishesSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    category=serializers.CharField()
    rating=serializers.FloatField()