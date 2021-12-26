from django.contrib import admin

from .models import AdvUser, Workout, SetWorkout, Repeated


admin.site.register(AdvUser)
admin.site.register(Workout)
admin.site.register(SetWorkout)
admin.site.register(Repeated)
