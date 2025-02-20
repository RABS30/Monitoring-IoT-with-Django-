from django.apps import AppConfig
import threading

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
    
    def ready(self):
        from dashboard.mqtt import startMqtt
        thread = threading.Thread(target=startMqtt, daemon=True)
        thread.start()
