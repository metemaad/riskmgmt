from django.shortcuts import render
from main_module.forms import (UserForm,ProfileUserInfoForm)




def register(request):
    registered = False

    if request.method == "POST":
        user_form=UserForm(data=request.POST)
        profile_form=ProfileUserInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=ProfileUserInfoForm()

    return render(request,'registeration/registeration.html',context={
    'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered,
    })
