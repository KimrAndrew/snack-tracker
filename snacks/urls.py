from django.urls import path, include
from .views import SnackPageView

urlpatterns = [
    path('',SnackPageView.as_view(), name='snacks')
]