from django.shortcuts import render
from .models import Wreck

def index(request):
  context = { 'wrecks_list': Wreck.objects.all() }
  return render(request, 'wrecks/index.html', context)
