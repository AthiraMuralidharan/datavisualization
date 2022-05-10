from django.urls import path
from data import views

urlpatterns = [
         path('test/',views.testing,name='testing'),

]