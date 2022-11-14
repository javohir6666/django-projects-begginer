from django.shortcuts import render, redirect

# Create your views here.
def homeView(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, 'chatapp/index.html')
