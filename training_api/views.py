from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import AdvUser, Repeated, Workout, SetWorkout
from .serializers import WorkoutSerializer, SetWorkoutSerializer


class ListListObjects(ListCreateAPIView):
    """
    Переопределяет метод create класса ListCreateAPIView
    для создания через Post запрос списка объектов
    """

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

    def get_queryset(self):
        params = self.request.query_params.dict()
        return super().get_queryset().filter(**params).all()


class WorkoutView(ListListObjects):
    """
    Одно упражнение
    Может передаваться информация об одном упражнении, так и информация о нескольких упражнениях в виде списка
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class SingleWorkoutView(RetrieveUpdateDestroyAPIView):
    """
    упражнение
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class SetWorkoutView(ListListObjects):
    """
    Одно упражнение
    Может передаваться информация об одном упражнении, так и информация о нескольких упражнениях в виде списка
    """
    queryset = SetWorkout.objects.all()
    serializer_class = SetWorkoutSerializer


class SingleSetWorkoutView(RetrieveUpdateDestroyAPIView):
    """
    упражнение
    """
    queryset = SetWorkout.objects.all()
    serializer_class = SetWorkoutSerializer
