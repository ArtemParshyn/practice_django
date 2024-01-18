from django.shortcuts import render


# Create your views here.
def index(request):



    context = {"name": "Artem"}
    return render(request, 'index.html', context)
