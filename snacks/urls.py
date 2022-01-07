from django.urls import path, include
from .views import SnackPageView, SnackListView

urlpatterns = [
    path('',SnackListView.as_view(), name='snacks')
]