from django.shortcuts import render
from django.views import View


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/auth/login.html')
    
    def post(self, request, *args, **kwargs):
        # login logic
        return render(request, 'frontend/auth/login.html')
    