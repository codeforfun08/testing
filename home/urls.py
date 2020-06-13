from django.contrib import admin
from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('',views.home,name="Home"),
    path('webdev',views.webdev,name="webdev"),
    path('programming',views.programming,name="programming"),

]   