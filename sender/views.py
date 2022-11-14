from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import SenderForm
from .models import EmailSender
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def send_message(request):
    if request.method == 'POST':
        email = request.POST["email"]
        theme = request.POST["theme"]
        message = request.POST["message"]
        