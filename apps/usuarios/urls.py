from django.conf.urls import url

from apps.usuarios.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    ##url(r'^solicitud/listar$', login_required(SolicitudList.as_view()), name='solicitud_listar'),
]