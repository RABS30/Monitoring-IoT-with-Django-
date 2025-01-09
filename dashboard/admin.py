from django.contrib import admin
from .models import sensorTanaman, opsiPerangkat, waktuPenyiraman

# Register your models here.
admin.site.register(sensorTanaman)
admin.site.register(opsiPerangkat)
admin.site.register(waktuPenyiraman)
