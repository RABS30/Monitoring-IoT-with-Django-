from django.contrib import admin
from .models import sensor,nilaiSensor,jenisPenyiraman, berdasarkanWaktu,berdasarkanSensor, opsiPerangkat

# Register your models here.
admin.site.register(sensor)
admin.site.register(nilaiSensor)
admin.site.register(jenisPenyiraman)
admin.site.register(berdasarkanWaktu)
admin.site.register(berdasarkanSensor)
admin.site.register(opsiPerangkat)
