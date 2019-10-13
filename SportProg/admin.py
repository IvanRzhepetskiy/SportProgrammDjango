from django.contrib import admin

# Register your models here.
from .models import Competitions, ParticipantsCompetitions, VideoPlots, Employees, Positions

admin.site.register(Competitions)
admin.site.register(ParticipantsCompetitions)

admin.site.register(VideoPlots)
admin.site.register(Employees)
admin.site.register(Positions)