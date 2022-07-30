from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from dishes.serializer import DishesSerializer
from dishes.models import Dishes


# Create your views here.

class DishesView(APIView):

    def get(self,request,*args,**kwargs):
        dishes=Dishes.objects.all()
        serialize=DishesSerializer(dishes,many=True)
        return Response(data=serialize.data)

    def post(self,request,*args,**kwargs):
        serialize=DishesSerializer(data=request.data)
        if serialize.is_valid():
            Dishes.objects.create(**serialize.validated_data)

            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)

class DishesDetailView(APIView):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dish=Dishes.objects.get(id=id)
        serialize=DishesSerializer(dish)
        return Response(data=serialize.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dish=Dishes.objects.get(id=id)
        serialize=DishesSerializer(dish)


