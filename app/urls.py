from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_patient', add_patient, name='add_patient'),
    path('delete_patient/<int:myid>/', delete_patient, name='delete_patient'),
    path('edite_patient/<int:myid>/', edite_patient, name='edite_patient'),
    path('update_patient/<int:myid>/', update_patient, name='update_patient'),

]
