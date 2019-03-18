from django.contrib import admin

# Register your models here.
from apps.registros.models import ticket

class ticket_model_admin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'estado',)
    search_fields = ('titulo', 'descripcion', 'estado',)

    list_filter = ('estado', 'fecha_creacion')

admin.site.register(ticket, ticket_model_admin)