from django.contrib import admin

from grzybyapp.models import Grzyby, Rodzina, Potrawa

admin.site.register(Rodzina)
admin.site.register(Potrawa)
admin.site.register(Grzyby)