from django.shortcuts import render
from django.shortcuts import redirect


def home(request):
    return render(request, "index.html")

def redirect_to_core(request):
    return redirect('/core/')


