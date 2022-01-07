from django.urls import path, include
from .views import SnackDetailView, SnackDetailView, SnackListView

urlpatterns = [
    path('',SnackListView.as_view(), name='snacks'),
    path('<int:pk>/',SnackDetailView.as_view(), name='snack_detail')
]