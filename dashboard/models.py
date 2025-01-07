from django.db import models

# Create your models here.
class sensorTanaman(models.Model):
    tanggal = models.DateTimeField(("Tanggal"), auto_now_add=True)
    nama    = models.CharField(("Nama Sensor"), max_length=50)
    nilai   = models.IntegerField(("Sensor"))
    
    class Meta:
        verbose_name = "Sensor Tanaman"
        verbose_name_plural = "Sensor Tanaman"
    
    def __str__(self):
        return f'{self.nama}, {self.nilai}, {self.tanggal.strftime("%d-%m-%Y, %H:%M")}'
        
    