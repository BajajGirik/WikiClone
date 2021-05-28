from django.urls import path
from . import views

app_name = "Encyclopedia"
urlpatterns = [
     path('', views.index, name="index"),
     path('contents', views.content, name="content"),
     path('random', views.random, name="random"),
     path('create', views.create, name="create"),
     path('wiki/<str:reqPage>', views.wiki, name="wiki")
]