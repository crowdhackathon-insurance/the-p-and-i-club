import re
import subprocess
import tempfile

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.utils import crypto

from clients.models import Client


gpg = settings.GPG


def verify_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        passphrase = crypto.get_random_string(20)
        data = {
            'client': client,
            'passphrase': passphrase
        }
        batch_input = loader.render_to_string(
            'clients/gpg_gen_key.txt', data
        )
        key = gpg.gen_key(batch_input)
        client.verified = True
        client.key_id = re.split(r'key (\w+) marked as', key.stderr)[1]
        client.key_fingerprint = key.fingerprint
        client.save()
        return HttpResponse('Client verified! Passphrase: %s' % passphrase, content_type='text/plain')
    else:
        data = {
            'client': client
        }
        return render(request, 'clients/verify_client.html', data)
