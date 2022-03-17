from django.urls import path

from .views import ComputerListCreateView, ComputerReadUpdateDeleteView

urlpatterns = [
    path('', ComputerListCreateView.as_view(), name='computers_list_create'),
    path('/<int:pk>', ComputerReadUpdateDeleteView.as_view(), name='computers_read_update_delete'),
]
