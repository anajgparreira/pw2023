from django.shortcuts import render


def base(request):
    return render(request, 'agenda/base.html')
# Create your views here.
