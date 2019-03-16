from django.shortcuts import render, redirect

def index(request):
    """
    Funcion que carga la vista para hacer login a la plataforma
    :param request (POST): username and password
    :return (template): login o home
    """
    data = dict()

    if request.method=='POST':
        print('Post')
    else:
        print('Get')

    return render(request,'index.html',data)


