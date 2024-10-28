from django.shortcuts import render
from django.http import HttpResponse
from .models import Pacjent, Wizyta

# Create your views here.
def index(request):
    pacjenci = Pacjent.objects.all()
    wizyty = Wizyta.objects.all()
    return render(request, 'goodDoctorApp/index.html', {'pacjenci': pacjenci, 'wizyty': wizyty})