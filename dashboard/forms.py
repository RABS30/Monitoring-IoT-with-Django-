from django import forms
from django.forms import ModelForm

from .models import berdasarkanSensor, jenisPenyiraman, berdasarkanWaktu, opsiPerangkat

# Opsi Perangkat
class formOpsiPerangkat(forms.ModelForm): 
    class Meta: 
        model  = opsiPerangkat 
        fields = ["jenisPenyiraman"]
        widgets= {
            'jenisPenyiraman' : forms.Select(attrs={'id' : 'jenisPenyiraman'})
        }
          
# Opsi Perangkat > Jenis Penyiraman
class formJenisPenyiraman(ModelForm):
    class Meta:
        model   = jenisPenyiraman
        fields  = ["nama"]
        widgets = {
            'nama': forms.Select(attrs={'class': 'form-control', 'id': 'jenisPenyiraman'}, 
                                 choices=(('Manual', 'Manual'),
                                          ('Berdasarkan Waktu', 'Berdasarkan Waktu'),
                                          ('Berdasarkan Sensor', 'Berdasarkan Sensor'),
                                          ))
        }    

# Opsi Perangkat >  Jenis Penyiraman > Berdasarkan Waktu
class formBerdasarkanWaktu(ModelForm):
    class Meta:
        model   = berdasarkanWaktu
        fields  = ["waktu"]
        widgets = {
            'waktu': forms.TimeInput(attrs={'class'     : 'form-control', 
                                            'id'        : 'waktu', 
                                            'format'    : '%H:%M',
                                            'type'      : 'time'})
        }
    
        
# Opsi Perangkat >  Jenis Penyiraman > Berdasarkan Sensor
class formBerdasarkanSensor(ModelForm):
    class Meta:
        model   = berdasarkanSensor
        fields  = ["sensor"]        
        
        
        
