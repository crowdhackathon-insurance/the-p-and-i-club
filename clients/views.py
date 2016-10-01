from django.http import HttpResponse
from django.shortcuts import render

from clients.models import Client


def verify_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.verified = True
        client.save()
        return HttpResponse('Verified!')
    else:
        data = {
            'client': client
        }
        return render(request, 'clients/verify_client.html', data)
