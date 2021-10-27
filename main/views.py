from django.shortcuts import render
from django.views.generic import View,ListView
from .models import *

# Create your views here.
class HomeView(ListView):
    def get(self,request):
        cats = Category.objects.all()
        context = {
            'cats':cats
        }
        return render(request,'index.html',context)

def cat_detail(request, slug):
    cat = Category.objects.get(slug=slug)
    context = {
        'cat':cat,
    }
    return render(request, 'index2.html', context)