import json

from django.shortcuts import render
from django.http import HttpResponse

def json_receiver(request):
  if request.method == 'POST':
    json = request.body
    print(json)
    return HttpResponse(json)
  else:
    return HttpResponse(f'It\'s working!<br><br>Method used: <b>{request.method}</b><br><br>You should use something like Insomnia to send a JSON via POST to test the essence of the project.<br>Download - <a href="https://insomnia.rest">Insomnia REST<a>')
