from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from dishes.serializer import DishesSerializer, DishesModelSerializer,UserSerializer
from dishes.models import Dishes
from rest_framework import status
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.contrib.auth.models import User
from rest_framework import authentication,permissions



# Create your views here.

class DishesView(APIView):

    def get(self, request, *args, **kwargs):
        dishes = Dishes.objects.all()
        serialize = DishesSerializer(dishes, many=True)
        return Response(data=serialize.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serialize = DishesSerializer(data=request.data)
        if serialize.is_valid():
            Dishes.objects.create(**serialize.validated_data)

            return Response(data=serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class DishesDetailView(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        dish = Dishes.objects.get(id=id)
        serialize = DishesSerializer(dish)
        return Response(data=serialize.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        serialize = DishesSerializer(data=request.data)
        if serialize.is_valid():

            Dishes.objects.filter(id=id).update(**serialize.validated_data)

            return Response(data=serialize.data, status=status.HTTP_202_ACCEPTED)

        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        dish = Dishes.objects.get(id=kwargs.get("id"))
        serializer = DishesSerializer(dish)
        dish.delete()
        return Response({"msg:Deleted"}, status=status.HTTP_200_OK)


class DishesModelView(APIView):

    def get(self, request, *args, **kwargs):

        dishes = Dishes.objects.all()
        serialize = DishesModelSerializer(dishes, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        dish = request.data
        serialize = DishesModelSerializer(data=dish)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DishesModelDetailView(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        dish = Dishes.objects.get(id=id)
        serialize = DishesModelSerializer(request.data)
        if serialize.data:
            return Response(data=serialize.data, status=status.HTTP_200_OK)
        else:
            return Response({"msg:Item Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        dish = Dishes.objects.get(id=id)
        serializer = DishesModelSerializer(instance=dish, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ViewSet

class DishViewSetView(ViewSet):
    def list(self, request, *args, **kwargs):

        dishes = Dishes.objects.all()
        serializer = DishesModelSerializer(dishes, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        dish = Dishes.objects.get(id=id)
        serilizer = DishesModelSerializer(dish)
        return Response(data=serilizer.data)

    def create(self, request, *args, **kwargs):
        dish = request.data
        serializer = DishesModelSerializer(data=dish)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.validated_data)
        else:
            return Response(data=serializer.errors)

    def update(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        dish = Dishes.objects.get(id=id)
        serialize = DishesSerializer(instance=dish, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.validated_data)
        else:
            return Response(data=serialize.errors)

    def destroy(self, request, *args, **kwargs):
        try:
            id = kwargs.get("pk")
            dish = Dishes.objects.get(id=id)
            dish.delete()
            return Response({"Msg:Item Deleted"})
        except:
            return Response({"msg:Item Not Found"})

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
