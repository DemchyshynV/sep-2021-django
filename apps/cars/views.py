from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer


# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         # qs = CarModel.objects.all().order_by('-price', '-brand')
#         # qs = CarModel.objects.all().order_by('-price').reverse()[:5]
#
#         # qs2 = qs.filter(brand__in=('bmw', 'audi'))
#         # qs2 = qs2.exclude(brand__iexact='bmw').count()
#         # print(qs2)
#         qs = CarModel.objects.all()
#         price_lt = self.request.query_params.get('price_lt', None)
#
#         if price_lt:
#             qs = qs.filter(price__lt=price_lt)
#
#         serializer = CarSerializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#
#         return Response(serializer.data, status.HTTP_201_CREATED)

class CarListCreateView(ListCreateAPIView):
    # queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        qs = CarModel.objects.all()
        price_lt = self.request.query_params.get('price_lt', None)
        if price_lt:
            qs = qs.filter(price__lt=price_lt)
        return qs


# class ReadUpdateDeleteView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#
#         # if not CarModel.objects.filter(pk=pk).exists():
#         #     return Response('Car with this id is not exists', status.HTTP_404_NOT_FOUND)
#         # car = CarModel.objects.get(pk=pk)
#         car = get_object_or_404(CarModel, pk=pk)
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         data = self.request.data
#
#         if not CarModel.objects.filter(pk=pk).exists():
#             return Response('Car with this id is not exists', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=pk)
#         serializer = CarSerializer(car, data=data)
#
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         data = self.request.data
#
#         if not CarModel.objects.filter(pk=pk).exists():
#             return Response('Car with this id is not exists', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=pk)
#         serializer = CarSerializer(car, data, partial=True)
#
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#
#         if not CarModel.objects.filter(pk=pk).exists():
#             return Response('Car with this id is not exists', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=pk)
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
