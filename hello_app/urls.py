from django.urls import path, include
from . import views

app_name = 'hello_app'
urlpatterns = [
    path('', views.hello, name='hello'),
    path('input/', views.input, name='input'),
    path('output/', views.output, name='output'),
]
