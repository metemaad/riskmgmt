from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse,reverse_lazy

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
