from django.urls import path

from .views import *

urlpatterns = [
    path('', dm_index),
    path('admin', admin),
    path('player', players_index),
    path('card', my_card),
    path('group', groups),
    path('clear_card', clear_card),
]