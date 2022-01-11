import pytest
from django.test import tag
from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase
from .models import AdvUser, Workout
# from .views import f
from django.test import Client
from .serializers import WorkoutSerializer

# **********************
# pytest --tb=no -v

#
# @pytest.mark.django_db
# @pytest.fixture()
# def my_user():
#     """Return answer to ultimate question."""
#     w = Workout.objects.create(name='test')
#     w.save()
#     return w
#
# @pytest.mark.django_db
# def test_my_user(my_user):
#     me = Workout.objects.get(name='test')
#     assert me

@pytest.mark.django_db
def test_client_01():
    c = Client()
    response = c.get('/api/workout')
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_02():
    valid_data = {
        "name": "name_0",
        "description": "description_0",
        "unit": "I",
    }
    c = Client()
    response = c.post('/api/workout', valid_data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_serialize_01():
    valid_data = {
        "name": "name_0",
        "description": "description_0",
        "unit": "I",
    }
    serializer = WorkoutSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_data
    assert serializer.data == valid_data
    assert serializer.errors == {}
