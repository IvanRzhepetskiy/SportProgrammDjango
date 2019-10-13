from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class ParticipantsCompetitions(models.Model):
    achievements = models.TextField(max_length=1000, blank=True)
    biography = models.TextField(max_length=3000, blank=True)
    interesting_facts = models.TextField(max_length=1000, blank=True)
    name = models.TextField(max_length=100, blank=True)
    second_name = models.TextField(max_length=100, blank=True)
    surname = models.TextField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Competitions(models.Model):
    name = models.TextField(max_length=500, blank=False)
    holding_date = models.DateField(null=True, blank=False)
    participants = models.ManyToManyField(ParticipantsCompetitions, related_name = 'related_competitions')


class Positions(models.Model):
    position_name = models.TextField(max_length=200)

    def __str__(self):
        return self.position_name

class Employees(models.Model):
    name = models.TextField(max_length=100)
    second_name = models.TextField(max_length=100)
    surname = models.TextField(max_length=100)
    birth_date = models.DateField()
    job_start_date = models.DateField()
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)


class VideoPlots(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    production_date = models.DateField()
    authors = models.ManyToManyField(Employees, related_name='related_video_plots')

    def __str__(self):
        return self.name


class Guests(models.Model):
    name = models.TextField(max_length=100)
    second_name = models.TextField(max_length=100)
    surname = models.TextField(max_length=100)
    birth_date = models.DateField()


class LivePrograms(models.Model):
    guests = models.ManyToManyField(Guests, related_name='related_live_programs')
    video_plots = models.ManyToManyField(VideoPlots, related_name='related_live_programs')
    name = models.TextField(max_length=100)
    live_date = models.DateField()

