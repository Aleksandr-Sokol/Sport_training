from django.contrib.postgres.indexes import GinIndex
from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    """
    Advanced user model for project
    """
    age = models.PositiveSmallIntegerField(null=True)
    sex = models.CharField(max_length=1,
                           choices=(('M', 'Male'), ('F', 'Female')),
                           blank=False,
                           default='M')
    height = models.PositiveSmallIntegerField(null=True)
    weight = models.PositiveSmallIntegerField(null=True)
    level = models.CharField(max_length=1,
                             choices=(('J', 'Junior'), ('M', 'Middle'), ('S', 'Senior')),
                             blank=False,
                             default='J')


class Workout(models.Model):
    name = models.CharField(max_length=120,
                            null=False,
                            # db_index=False,
                            )
    description = models.TextField(null=True,
                                   blank=True,
                                   # db_index=False,
                                   )
    unit = models.CharField(max_length=1,
                            choices=(('I', 'Iteration'), ('T', 'Time')),
                            blank=False,
                            default='I',
                            )

    class Meta:
        indexes = [GinIndex(fields=['name', 'description'])]

    def __str__(self):
        return f'{self.name}, unit is {self.unit}'


class SetWorkout(models.Model):
    name = models.CharField(max_length=120, null=False)

    user = models.ForeignKey(AdvUser,
                             related_name='set_workout',
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False)

    work = models.ManyToManyField(Workout, through='Repeated', through_fields=('set', 'work'), )

    def __str__(self):
        return f'{self.name}'


class Repeated(models.Model):
    work = models.ForeignKey(Workout,
                             on_delete=models.CASCADE,
                             )
    set = models.ForeignKey(SetWorkout,
                            on_delete=models.CASCADE,
                            )
    repeat = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.set} - {self.work} > {self.repeat}'
