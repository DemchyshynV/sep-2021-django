from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListAPIView):
    """
    Get all cars with filters
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter


class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get Car by id
    put:
        Update car by id
    patch:
        Partial update car by id
    delete:
        Delete car by id
    """
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
