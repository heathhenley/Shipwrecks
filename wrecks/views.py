from django.shortcuts import render
from .models import Wreck

def index(request):
  context = { 'wrecks_list': list(Wreck.objects.all().values()) }
  return render(request, 'wrecks/index.html', context)
