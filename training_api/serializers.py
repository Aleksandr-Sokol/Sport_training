from django.db.models import CharField
from rest_framework import serializers
from rest_framework.fields import Field

from .models import AdvUser, Repeated, Workout, SetWorkout

from django.core.exceptions import ObjectDoesNotExist


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'


class SetWorkoutSerializer(serializers.ModelSerializer):
    work = WorkoutSerializer(many=True, read_only=False)

    class Meta:
        model = SetWorkout
        fields = '__all__'
