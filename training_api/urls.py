from django.urls import path
from training_api.views import WorkoutView, SingleWorkoutView

app_name = "training_api"

urlpatterns = [
    path('workout', WorkoutView.as_view()),
    path('workout/<int:pk>', SingleWorkoutView.as_view()),
]