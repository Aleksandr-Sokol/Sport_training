from django.urls import path
from training_api.views import WorkoutView, SingleWorkoutView, SetWorkoutView, SingleSetWorkoutView

app_name = "training_api"

urlpatterns = [
    path('workout', WorkoutView.as_view()),
    path('workout/<int:pk>', SingleWorkoutView.as_view()),
    path('set_workout', SetWorkoutView.as_view()),
    path('set_workout/<int:pk>', SingleSetWorkoutView.as_view()),
]