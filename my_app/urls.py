from django.urls import path
from . import views

app_name = 'my_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_note/', views.add_note, name='add_note'),
]