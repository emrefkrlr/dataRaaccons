from django.shortcuts import render

# Create your views here.

def dashboard(request):

    response = render(request, 'raccoon_analytic/pages/dashboard.html')

    return response