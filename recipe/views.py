from django.shortcuts import render
from .models import *


def MenuView(request):
    all_items = Menu.objects.all()
    return render(request, 'recipe/menu.html' , {'item_name':all_items})

def RecipeKharabath(request):   
    steps = Kharabath.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipeKesaribath(request):   
    steps = Kesaribath.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipeRoundIdli(request):   
    steps = RoundIdli.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipeTatteIdli(request):   
    steps = TatteIdli.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipeRiceBath(request):   
    steps = RiceBath.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipeBisibelebath(request):   
    steps = Bisibelebath.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipePuliyogare(request):   
    steps = Puliyogare.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipeAvalakki(request):   
    steps = Avalakki.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipeMandakki(request):   
    steps = Mandakki.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipeUddinaVada(request):   
    steps = UddinaVada.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipeMasalaVada(request):   
    steps = MasalaVada.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipeDosaD(request):   
    steps = DosaD.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipePaddu(request):   
    steps = Paddu.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})

def RecipeGeneric(request):   
    steps = Generic.objects.all()
    return render(request , 'recipe/detail_view.html' , {'process':steps})