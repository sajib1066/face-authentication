from django.views.generic import View
from django.shortcuts import render, redirect


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
