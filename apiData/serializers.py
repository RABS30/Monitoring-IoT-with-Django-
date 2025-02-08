from dashboard.models import sensor, nilaiSensor
from rest_framework import serializers
from django.utils import timezone
from django.db.models.functions import Trunc, TruncMinute,TruncHour, TruncDay, TruncMonth
from django.db.models import Avg



class sensorSerializer(serializers.ModelSerializer):
    nilai = serializers.SerializerMethodField()
    waktu = serializers.SerializerMethodField()

    class Meta:
        model = sensor
        fields = ['nama', 'nilai', 'waktu']
        
    def getTimeRange(self):
        request = self.context.get('request')
        print(f'ini request : {request}')
        
        timeRange   = request.query_params.get('range', 'daily') #type:ignore
        now         = timezone.now()
        
        if timeRange == 'weekly' :
            return now - timezone.timedelta(days=7), TruncHour('waktu')
        elif timeRange == 'mountly' :
            return now - timezone.timedelta(days=30), TruncDay('waktu')
        elif timeRange == 'yearly' :
            return now - timezone.timedelta(days=365), TruncDay('waktu')
        else :
            return now.replace(hour=0, minute=0, second=0, microsecond=0), TruncMinute('waktu')

    def get_nilai(self, obj):
        timeRange, truncateTime = self.getTimeRange()
        nilai = obj.nilaiSensor.filter(waktu__gte=timeRange)
        nilai = nilai.annotate(timeGroup=truncateTime).values('timeGroup').annotate(avgValue=Avg('nilai')).order_by('timeGroup')

        # Mengembalikan daftar nilai rata-rata per menit
        return [int(data['avgValue']) for data in nilai]

    def get_waktu(self, obj):
        timeRange, truncateTime = self.getTimeRange()
    
        
        # Ambil waktu data sensor
        nilai = obj.nilaiSensor.filter(waktu__gte=timeRange)
        nilai = nilai.annotate(timeGroup=truncateTime).values('timeGroup').annotate(avgValue=Avg('nilai')).order_by('timeGroup')

        # Format waktu ke 'HH:MM'
        return [data['timeGroup'].strftime('%H:%M') for data in nilai]
