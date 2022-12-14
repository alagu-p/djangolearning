from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from validate_email import validate_email


class RegistrationView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        data = request.POST
        print(data)
        email = request.POST.get('email')
        return render(request, 'auth/register.html', context={'data': data})
