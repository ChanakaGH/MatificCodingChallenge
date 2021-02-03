from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Task)
admin.site.register(Team)
admin.site.register(Coach)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Scorecard)
admin.site.register(Participation)