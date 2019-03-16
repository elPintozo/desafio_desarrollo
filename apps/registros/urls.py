from django.conf.urls import url

from apps.registros.views import ticket_crear, ticket_listar, ticket_detalle

urlpatterns = [
    url(r'^listar$', ticket_listar, name='ticket-listar'),
    url(r'^crear$', ticket_crear, name='ticket-crear'),
    url(r'^detalle/(?P<pk_ticket>\d+)$', ticket_detalle, name='ticket-detalle'),
]