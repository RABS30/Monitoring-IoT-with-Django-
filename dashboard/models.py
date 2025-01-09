from random import choice
from typing import Any, Iterable
from django.db import models


# Create your models here.
class sensorTanaman(models.Model):
    tanggal = models.DateTimeField(("Tanggal"), auto_now_add=False)
    nama    = models.CharField(("Nama Sensor"), max_length=50)
    nilai   = models.IntegerField(("Sensor"))
    
    class Meta:
        verbose_name = "Sensor Tanaman"
        verbose_name_plural = "Sensor Tanaman"
    
    def __str__(self):
        return f'{self.nama}, {self.nilai}, {self.tanggal.strftime("%d-%m-%Y, %H:%M")}'
    
class opsiPerangkat(models.Model):
    jenisPenyiraman = models.CharField(("Penyiraman"), 
                                       max_length=50, 
                                       choices=(('manual', 'Manual'), 
                                                ('aturWaktu' , 'Atur Waktu'), 
                                                ('berdasarkanSensor' , 'Berdasarkan Sensor')),)
    
    
    jenisPengisianTangkiAir = models.CharField(("Pengisian Tangki Air"), 
                                               max_length=50, 
                                               choices=(('manual', 'Manual'), 
                                                        ('berdasarkanVolume' , 'Berdasarkan Volume')),
                                                        )
    
    def __str__(self) :
        return f'id: {self.pk} penyiraman : {self.jenisPenyiraman}, pengisian tangki : {self.jenisPengisianTangkiAir}'
        
class waktuPenyiraman(models.Model):
    opsiPerangkat = models.ForeignKey('opsiPerangkat', on_delete = models.CASCADE, related_name='waktuPenyiraman', editable=False, blank=True)
    waktu         = models.TimeField(("Waktu"))
    
    
    def save(self):
        self.opsiPerangkat = opsiPerangkat.objects.get(id=1)
        return super().save()
    
    def __str__(self):
        return f'waktu : {self.waktu}, {self.opsiPerangkat.jenisPenyiraman}'
    
    
class berdasarkanSensor(models.Model):
    opsiPerangkat = models.OneToOneField("dashboard.opsiPerangkat", verbose_name=("Opsi"), on_delete=models.CASCADE)
    sensor        = models.CharField(("Sensor"), max_length=50)
    
    
    def __str__(self):
        return f'sensor : {self.sensor}, opsi: {self.opsiPerangkat.jenisPenyiraman}'
    
