from django.shortcuts import render
from django.views.generic import View,ListView

# Create your views here.
class HomeView(ListView):
    def get(self,request):
        return render(request,'index.html')