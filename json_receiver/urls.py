from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views

urlpatterns = [
  # API
    path('receive_json/', csrf_exempt(views.json_receiver)),
]
