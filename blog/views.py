from django.shortcuts import render
from django.http import HttpResponse


# colocamos o index, pois esse é o primeiro arquivo a ser chamado
def index(request):  # sempre usaremos nesse método uma request que é uma convenção
    return HttpResponse('Olá Mundo!')
