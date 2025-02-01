from django.contrib import admin
from .models import sensor,nilaiSensor,jenisPenyiraman, berdasarkanWaktu,berdasarkanSensor, opsiPerangkat, jenisPengisianAir, jenisPemberianPupuk, pemberianPupukTerakhir, penyiramanTerakhir, tanggalTanaman

# Register your models here.
admin.site.register(sensor)
admin.site.register(nilaiSensor)
admin.site.register(jenisPenyiraman)
admin.site.register(berdasarkanWaktu)
admin.site.register(berdasarkanSensor)
admin.site.register(opsiPerangkat)
admin.site.register(jenisPengisianAir)
admin.site.register(jenisPemberianPupuk)
admin.site.register(penyiramanTerakhir)
admin.site.register(pemberianPupukTerakhir)
admin.site.register(tanggalTanaman)
