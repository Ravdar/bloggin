from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # login(request, new_user)
            return redirect("mainapp:main_view")
    else:
        form = UserCreationForm()
    return render(request, "registration/registration.html", {"form":form})


