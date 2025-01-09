from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
from django.forms.utils import ErrorList

from .models import opsiPerangkat, waktuPenyiraman


class formsOpsiPerangkat(ModelForm):        
    class Meta:
        model   = opsiPerangkat
        fields  = ['jenisPenyiraman', 'jenisPengisianTangkiAir']

        widgets = {
                'jenisPenyiraman'   : forms.Select(attrs={'id':'jenisPenyiraman',
                                                           'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
                
                'jenisPengisianTangkiAir' : forms.Select(attrs={'id':'jenisPengisianTangkiAir',
                                                                            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        }
        
        
        
class formsWaktuPenyiraman(ModelForm):
    class Meta:
        model   = waktuPenyiraman
        fields  = ['waktu']
        
        