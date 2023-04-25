from django.contrib import admin
from .models import PracovniZkusenost, Projekt, Vzdelani

# Register your models here.

admin.site.register(Vzdelani)
admin.site.register(Projekt)
admin.site.register(PracovniZkusenost)
