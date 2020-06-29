from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            #if user.is_active():
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
            #else:
            #    return HttpResponse("account is not active")
        else:
            print("login failed.....")
            return HttpResponse("Invalid login")
    else:
        return render(request,'registeration/login.html',{})
