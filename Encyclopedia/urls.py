from django.urls import path
from . import views

app_name = "Encyclopedia"
urlpatterns = [
     path('', views.index, name="index")
]