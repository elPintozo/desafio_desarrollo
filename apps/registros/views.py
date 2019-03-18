import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db.models.functions import ExtractDay
from django.shortcuts import render, redirect
from apps.registros.forms import ticket_form
from apps.registros.models import ticket

@login_required()
def ticket_crear(request):
    """
    View habilitada para crear un ticket
    :param request (POST): formulario ticket_form
    :return (template): vista crear o listar
    """

    ## Variable que almacena las variable para template
    data = dict()

    if request.method == 'POST':
        form = ticket_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registros_namespace:ticket-listar')
    else:
        form = ticket_form()


    data['form'] = form

    return render(request, 'registros/ticket_crear.html', data)


@login_required()
def ticket_listar(request):
    """
    View habilitada para listar ticket
    :param request (): -
    :return (template): listar
    """

    ## Variable que almacena las variable para template
    data = dict()

    ## Obtengo los ticket y agrego en la queryset los dias transcurridos desde su publicacion
    data['lista_ticket'] = ticket.objects.annotate(dias_transcurridos=ExtractDay(datetime.datetime.now()-F('fecha_creacion')))

    return render(request, 'registros/ticket_listar.html', data)

@login_required()
def ticket_detalle(request, pk_ticket):
    """
    View habilitada para mostar los detalles de un ticket
    :param request (): -
    :param pk_ticket (int): pk de un ticket
    :return (template): detalles
    """

    ## Variable que almacena las variable para template
    data = dict()

    ticket_solicitado = ticket.objects.filter(pk=int(pk_ticket))

    ##Valido si se encontro el ticket solicitado
    if ticket_solicitado.count()!=0:
        data['form']=ticket_form(instance=ticket_solicitado[0])
        data['ticked_id'] = ticket_solicitado[0].pk

    ## Si el ticket no se encontro se vuelve a la vista de listar
    else:
        ##Se notifica al usuario que no existe el ticket pedido
        data['mensaje'] = 'Ticket no encontrado'
        return render(request, 'registros/ticket_listar.html', data)

    return render(request, 'registros/ticket_detalle.html', data)













