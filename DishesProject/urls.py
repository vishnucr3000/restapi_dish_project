"""DishesProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dishes.views import DishesView,DishesDetailView,DishesModelView,DishesModelDetailView,DishViewSetView,UserView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('dishesviewset',DishViewSetView,basename="Dishes")
router.register('dishes/users',UserView,basename="users")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dishes',DishesView.as_view()),
    path('dishes/<int:id>',DishesDetailView.as_view()),
    path('dishmodels',DishesModelView.as_view()),
    path('dishesmodeldetails/<int:id>',DishesModelDetailView.as_view())
]+router.urls
