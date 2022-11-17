from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def aPage(request):
    return HttpResponse('ok')
 