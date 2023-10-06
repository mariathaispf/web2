from django.shortcuts import render

# Create your views here.
def norte (request):
    return render (request, 'norte.html')
def amazonas (request):
    return render (request, 'amazonas.html')
def para (request):
    return render (request, 'para.html')
def tocantins (request):
    return render (request, 'tocantins.html')
def voltar (request):
    return render (request, 'index.html')
