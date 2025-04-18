from django.db import models

# Sensor 
class sensor(models.Model):
    nama    = models.CharField(("Nama Sensor"), max_length=50)
    
    class Meta:
        verbose_name = "Sensor"
        verbose_name_plural = "Sensor"
    
    def __str__(self):
        return f'{self.nama}'
    
# Sensor > Nilai Sensor
class nilaiSensor(models.Model):
    sensor  = models.ForeignKey("dashboard.sensor", 
                                on_delete=models.CASCADE, 
                                related_name='nilaiSensor')
    
    nilai   = models.IntegerField(("Nilai"))
    
    waktu   = models.DateTimeField(("Waktu"), auto_now_add=True)
    
    class Meta :
        verbose_name = 'Sensor > Nilai Sensor'
        verbose_name_plural = "Sensor > Nilai Sensor"
        
    def __str__(self):
        return f'{self.waktu.strftime("%d-%m-%Y %H:%M")} WIB : {self.sensor.nama} \t\t: {self.nilai}'
    
    
    
# jenis Penyiraman
class jenisPenyiraman(models.Model):
    nama = models.CharField(("Jenis Penyiraman"), 
                            max_length=50,
                            unique=True,  
                            choices=(('Manual', 'Manual'),
                                     ('Berdasarkan Waktu', 'Berdasarkan Waktu'),
                                     ('Berdasarkan Sensor', 'Berdasarkan Sensor'))
                            )

    class Meta:
        verbose_name = "Opsi Perangkat > Jenis Penyiraman"
        verbose_name_plural = "Opsi Perangkat > Jenis Penyiraman"
        
    def __str__(self) :
        return f'{self.nama}'

# Jenis Penyiraman > berdasarkan waktu
class berdasarkanWaktu(models.Model):
    opsiPerangkat = models.ForeignKey('dashboard.jenisPenyiraman', 
                                      on_delete = models.CASCADE, 
                                      related_name='berdasarkanWaktu', 
                                      editable=False, 
                                      blank=True)
    
    waktu         = models.TimeField(("Waktu"), 
                                     null=True, 
                                     blank=True,)
    
    class Meta:
        verbose_name = "Opsi Perangkat > Jenis Penyiraman > Berdasarkan Waktu"
        verbose_name_plural = "Opsi Perangkat > Jenis Penyiraman > Berdasarkan Waktu"
    
    
    def save(self):
        self.opsiPerangkat = jenisPenyiraman.objects.get(nama='Berdasarkan Waktu')
        return super().save()
    
    def __str__(self):
        return f'ID : {self.pk}. waktu : {self.waktu}, {self.opsiPerangkat.nama}'
 
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
        verbose_name = "Opsi Perangkat > Jenis Penyiraman > Berdasarkan Sensor"
        verbose_name_plural = "Opsi Perangkat > Jenis Penyiraman > Berdasarkan Sensor"
    
    
    def save(self):
        self.opsiPerangkat = jenisPenyiraman.objects.get(nama='Berdasarkan Sensor')
        return super().save()
    
    def __str__(self):
        return f'ID : {self.pk}, sensor : {self.sensor}'
    
        


# Jenis Pengisian Air
class jenisPengisianAir(models.Model):
    nama = models.CharField(("Jenis Pengisian Air"), 
                            max_length=50,
                            choices=(
                                ('Otomatis', 'Otomatis'),
                                ('Manual', 'Manual'),
                                ),
                            unique=True
                            )
    
    class Meta :
        verbose_name = "Opsi Perangkat > Jenis Pengisian Air"
        verbose_name_plural = "Opsi Perangkat > Jenis Pengisian Air"
    
    def __str__(self):
        return f"{self.nama}"
    


# Jenis Pemberian Pupuk
class jenisPemberianPupuk(models.Model):
    nama = models.CharField(("Jenis Pemberian Pupuk"),
                            max_length=50,
                            choices=(
                                ('Otomatis', 'Otomatis'),
                                ('Manual', 'Manual'),
                                ),
                            unique=True,
                            
                            )
    
    class Meta:
        verbose_name = "Opsi Perangkat > Jenis Pemberian Pupuk"
        verbose_name_plural = "Opsi Perangkat > Jenis Pemberian Pupuk"
        
    def __str__(self):
        return f'{self.nama}'
    
    

# Opsi 
class opsiPerangkat(models.Model):
    jenisPenyiraman     = models.OneToOneField("dashboard.jenisPenyiraman", 
                                           verbose_name=("Jenis Penyiraman"), 
                                           on_delete=models.CASCADE)
    
    jenisPengisianAir   = models.OneToOneField("dashboard.jenisPengisianAir", 
                                               verbose_name=("Jenis Pengisian Tangki Air"), 
                                               on_delete=models.CASCADE)
    
    jenisPemberianPupuk = models.OneToOneField("dashboard.jenisPemberianPupuk", 
                                               verbose_name=("Jenis Pemberian Pupuk"), 
                                               on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Opsi Perangkat"
        verbose_name_plural = "Opsi Perangkat"
    
    
    def __str__(self) :
        return f'{self.pk}. Jenis Penyiraman : {self.jenisPenyiraman}'
    
    
# Informasi > Penyiraman Terkahir
class penyiramanTerakhir(models.Model):
    waktu  = models.DateTimeField(("Waktu"), auto_now=True)
    
    class Meta :
        verbose_name = "Informasi > Penyiraman Terakhir"
        verbose_name_plural = "Informasi > Penyiraman Terakhir"
        
    def __str__(self):
        return f'Penyiraman Terakhir : {self.waktu.strftime("%A, %d %B %Y, %H:%M")}'
    
    
# Informasi > Penyiraman Terkahir
class pemberianPupukTerakhir(models.Model):
    waktu  = models.DateTimeField(("Waktu"), auto_now=True)
    
    class Meta :
        verbose_name = "Informasai > Pemberian Pupuk Terkahir"
        verbose_name_plural = "Informasai > Pemberian Pupuk Terkahir"
        
    def __str__(self):
        return f'Pemberian Pupuk Terakhir : {self.waktu.strftime("%A, %d %B %Y, %H:%M")}'
    
# Informasi > Penanaman Tanaman
class tanggalTanaman(models.Model):
    nama    = models.CharField(("Nama Tanaman"), max_length=50)
    tanggal = models.DateField(("Tanggal Penanaman"))
    
    class Meta :
        verbose_name = "Informasi > Penanaman Tanaman"
        verbose_name_plural = "Informasi > Penanaman Tanaman"
    
    def __str__(self) :
        return f'{self.nama} - {self.tanggal.strftime("%A, %d %B %Y %H:%M WIB")}'
    
    
    
    
    
    
    