from django.contrib import admin

from .models import Inductors, TubeShapes, Machines, TestInductor

# Register your models here.

admin.site.register(Inductors)
admin.site.register(TubeShapes)
admin.site.register(Machines)
admin.site.register(TestInductor)
