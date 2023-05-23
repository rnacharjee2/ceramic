from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home-page'),
    path('jigger-production-entry/', jiggerProductionEntry,
         name="jigger-production-entry")
]
