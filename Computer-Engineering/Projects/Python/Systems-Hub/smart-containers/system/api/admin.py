from django.contrib import admin
from .models import Container, Telemetria

@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'criado_em')
    search_fields = ('codigo',)

@admin.register(Telemetria)
class TelemetriaAdmin(admin.ModelAdmin):
    list_display = ('container', 'status_porta', 'temperatura', 'latitude', 'longitude', 'data_hora')
    list_filter = ('status_porta', 'data_hora')
    search_fields = ('container__codigo',)
