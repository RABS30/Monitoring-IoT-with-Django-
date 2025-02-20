from django import forms
from django.forms import ModelForm

from .models import berdasarkanSensor, jenisPenyiraman, berdasarkanWaktu, opsiPerangkat

# Opsi Perangkat
class formOpsiPerangkat(forms.ModelForm): 
    class Meta: 
        model  = opsiPerangkat 
        fields = ["jenisPenyiraman", "jenisPengisianAir", "jenisPemberianPupuk"]
        widgets= {
            'jenisPenyiraman' : forms.Select(attrs={'id' : 'jenisPenyiraman', 'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            
            'jenisPengisianAir' : forms.Select(attrs={'id' : 'jenisPengisianAir', 'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),            
            
            'jenisPemberianPupuk' : forms.Select(attrs={'id' : 'jenisPemberianPupuk', 'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
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
            'waktu': forms.TimeInput(attrs={
                'class' : 'rounded-none rounded-s-lg bg-gray-50 border text-gray-900 leading-none focus:ring-blue-500 focus:border-blue-500 block flex-1 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 
                'min': '00:00',
                'max': '24:00', 
                'id' : 'waktu', 
                'format' : '%H:%M',
                'type' : 'time'})
        }
    
        
# Opsi Perangkat >  Jenis Penyiraman > Berdasarkan Sensor
class formBerdasarkanSensor(ModelForm):
    class Meta:
        model   = berdasarkanSensor
        fields  = ["sensor"]      
        widgets = {
            'sensor': forms.Select(attrs={'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'id': 'sensor'},)
        }  
        
