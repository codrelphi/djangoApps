from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def message(request):
    message= """
        <h1>Message</h1>
        <p>Un message est un ensemble de signes. Il implique donc un codage par l'émetteur, et un décodage par le récepteur
        (d'où la nécessité d'un code commun). La théorie de l'information fut mise au point pour déterminer mathématiquement
        le taux d’information transmis dans la communication d’un message par un canal de communication, notamment en présence
        de parasites appelés bruits. Il fut repris par Roman Jakobson pour étayer la théorie linguistique.</p>
    """
    return HttpResponse(message)
