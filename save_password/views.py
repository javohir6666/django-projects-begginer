from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import User, SavePassword
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.
class Index(View):
    def get(self, request):
        if 'user' in request.session:
            get_save_pwd = SavePassword.objects.filter(user__name=request.session['user']).order_by('-id')

            account_pwd = User.objects.get(name=request.session['user'])

            params = {'passwords': get_save_pwd, 'user_account': account_pwd}
            return render(request, 'save_password/show_pwd.html', params)
        else:
            return render(request, 'save_password/index.html')


    def post(self, request):
        uname = request.POST['user_name']
        pwd = request.POST['password']

        if uname and pwd:
            create_user = User.objects.create(name=uname, pwd=pwd)
            create_user.save()
            return render(request, 'save_password/index.html')
        else:
            error = "Please Fill the fields."
            return render(request, 'save_password/show_pwd.html', {'error': error})




class Login(View):
    def get(self, request):
        return render(request, 'save_password/login.html')

    def post(self, request):
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        try:
            user_obj = User.objects.get(name=uname, pwd=pwd)
            request.session['user'] = user_obj.name
        except:
            return redirect('login')

        return redirect('index')


class Logout(View):
    def get(self, request):
        del request.session['user']
        return redirect('index')


class SavePwd(View):
    def get(self, request):
        return render(request, 'save_password/save_pwd.html')

    def post(self, request):
        title = request.POST['title']
        pwd = request.POST['pwd']

        makePwd = make_password(pwd)

        user_obj = User.objects.get(name=request.session['user'])
        savePwd = SavePassword.objects.create(user=user_obj, title=title, pwd=pwd, hide_pwd=makePwd)
        savePwd.save()

        return redirect('save_pwd')


class Edit(View):
    def get(self, request, id):
        pwd_id_obj = SavePassword.objects.get(id=id)
        params = {'obj': pwd_id_obj}
        return render(request, 'save_password/edit.html', params)

    def post(self,request, id):
        pwd_obj = SavePassword.objects.get(id=id)

        new_title = request.POST['title']
        new_pwd = request.POST['pwd']
        new_pwd_hash = make_password(new_pwd)

        pwd_obj.title = new_title
        pwd_obj.pwd = new_pwd
        pwd_obj.hide_pwd = new_pwd_hash

        pwd_obj.save()

        return redirect('index')