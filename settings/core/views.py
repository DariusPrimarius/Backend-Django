from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def aPage(request):
    #user:User = User.objects.get(pk=1)
    username = request.POST.get("username")
    email = request.POST.get("email")
    return JsonResponse({   "username":username,
                            "email":email  })
 