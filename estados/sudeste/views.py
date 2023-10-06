from django.shortcuts import render

# Create your views here.
def sudeste (request):
    return render (request, 'sudeste.html')
def espirito_santo (request):
    return render (request, 'espirito_santo.html')
def minas_gerais (request):
    return render (request, 'minas_gerais.html')
def voltar (request):
    return render (request, 'index.html')