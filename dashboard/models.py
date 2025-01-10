from django.db import models

# Sensor 
class sensor(models.Model):
    nama    = models.CharField(("Nama Sensor"), max_length=50)
    
    class Meta:
        verbose_name = "Sensor"
        verbose_name_plural = "Sensor"
    
    def __str__(self):
        return f'{self.pk} : {self.nama}'
# Sensor > Nilai Sensor
class nilaiSensor(models.Model):
    sensor  = models.ForeignKey("dashboard.sensor", 
                                on_delete=models.CASCADE, 
                                related_name='sensor')
    nilai   = models.IntegerField(("Nilai"))
    
    class Meta :
        verbose_name = 'Sensor > Nilai Sensor'
        verbose_name_plural = "Sensor > Nilai Sensor"
    def __str__(self):
        return f'{self.pk} : {self.sensor.nama} : {self.nilai}'
    
    
    
# jenis Penyiraman
class jenisPenyiraman(models.Model):
    nama = models.CharField(("Jenis Penyiraman"), 
                            max_length=50, 
                            choices=(('manual', 'Manual'),
                                     ('berdasarkanWaktu', 'Berdasarkan Waktu'),
                                     ('berdasarkanSensor', 'Berdasarkan Sensor'))
                            )

    class Meta:
        verbose_name = "Jenis Penyiraman"
        verbose_name_plural = "Jenis Penyiraman"
        
    def __str__(self) :
        return f'id: {self.pk} penyiraman : {self.nama}'

# Jenis Penyiraman > berdasarkan waktu
class berdasarkanWaktu(models.Model):
    opsiPerangkat = models.ForeignKey('dashboard.jenisPenyiraman', 
                                      on_delete = models.CASCADE, 
                                      related_name='berdasarkanWaktu', 
                                      editable=False, 
                                      blank=True)
    
    waktu         = models.TimeField(("Waktu"), 
                                     null=True, 
                                     blank=True)
    
    class Meta:
        verbose_name = "Jenis Penyiraman > Berdasarkan Waktu"
        verbose_name_plural = "Jenis Penyiraman > Berdasarkan Waktu"
    
    
    def save(self):
        self.opsiPerangkat = jenisPenyiraman.objects.get(nama='berdasarkanWaktu')
        return super().save()
    
    def __str__(self):
        return f'{self.pk}. waktu : {self.waktu}'
 
# Jenis Penyiraman > berdasarkan Sensor
class berdasarkanSensor(models.Model):
    opsiPerangkat   = models.OneToOneField("dashboard.jenisPenyiraman", 
                                      verbose_name=("Opsi"), 
                                      on_delete=models.CASCADE, 
                                      editable=False, 
                                      )
    
    sensor          = models.OneToOneField("dashboard.sensor", 
                                           verbose_name=("Nama Sensor"), 
                                           on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Jenis Penyiraman > Berdasarkan Sensor"
        verbose_name_plural = "Jenis Penyiraman > Berdasarkan Sensor"
    
    
    def save(self):
        self.opsiPerangkat = jenisPenyiraman.objects.get(nama='berdasarkanSensor')
        return super().save()
     
    # def __init__(self):
    #     sets = set(sensorTanaman.objects.values_list('nama', flat=True))
    #     choices = []
    #     for data in sets :
    #         choices.append((data, data))
            
    #     self._meta.get_field('sensor').choices = tuple(choices)
    #     super().__init__()
        
    def __str__(self):
        return f'ID : {self.pk}, sensor : {self.sensor}'
    


