from django.shortcuts import render
from django.views.generic import View,ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(LoginRequiredMixin,ListView):
    def get(self,request):
        return render(request,'index.html')