from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


# Create your views here.
def index(request):
    patient_list = Patient.objects.all()
    context = {
        'patient_list': patient_list
    }
    return render(request, 'index.html', context)


def add_patient(request):
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        type = request.POST['type']
        date = request.POST['date']
        patient = Patient(nom=nom, prenom=prenom, type=type, date=date)
        patient.save()
        messages.info(request, "added sucessfully")
    else:
        pass

    patient_list = Patient.objects.all()
    context = {
        'patient_list': patient_list
    }
    return render(request, 'index.html', context)


def delete_patient(request, myid):
    patient = Patient.objects.get(id=myid)
    patient.delete()
    messages.info(request, "deleted successfully")
    return redirect(index)


def edite_patient(request, myid):
    sel_patient = Patient.objects.get(id=myid)
    patient_list = Patient.objects.all()
    context = {
        'sel_patient': sel_patient,
        'patient_list': patient_list
    }
    return render(request, 'index.html', context)


def update_patient(request, myid):
    patient = Patient.objects.get(id=myid)
    patient.prenom = request.POST['prenom']
    patient.nom = request.POST['nom']
    patient.type = request.POST['type']
    patient.date = request.POST['date']
    patient.save()
    messages.info(request,"updated")
    return redirect('index')
