from django.shortcuts import render
from .models import Grzyby

def index(request):
    grzyby = Grzyby.objects.all()
    return render(request, 'index.html', {'grzyby': grzyby})