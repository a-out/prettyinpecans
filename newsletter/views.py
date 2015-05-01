from django.shortcuts import render
from django.http import HttpResponse

from .models import Subscriber
from .utils import subscribe_user

import json

def subscribe(request):
    data = json.loads(request.body.decode('utf-8'))
    email = data['email']

    if Subscriber.objects.filter(email=email).exists():
        response = HttpResponse()
        response.status_code = 401
        return response
    else:
        Subscriber.objects.create(email=email)
        subscribe_user(email)
        return HttpResponse()