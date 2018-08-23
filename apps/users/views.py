# _*_ coding:utf-8 _*_

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifypwdForm
from utils.email_send import send_rigister_email


class ActiveUserView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_failed.html')
        return render(request, 'login.html')


class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form":register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get("email","")
            password = request.POST.get("password","")
            if UserProfile.objects.filter(email=username):
                return render(request, "register.html", {"register_form": register_form, "msg": "此邮箱已被注册！"})
            user = UserProfile()
            user.username = username
            user.is_active = False
            #对密码进行加密
            user.password = make_password(password)
            user.email = username
            user.save()

            send_rigister_email(username,'register')
            return render(request,"login.html")
        else:
            return render(request, 'register.html', {"register_form":register_form})


class CustomBackend(ModelBackend):
    #自定义登录验证
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    #用类来实现视图
    def get(self,request):
        return render(request, "login.html", {})

    def post(self,request):
        login_form = LoginForm(request.POST)
        #判断login_form内是否存在_errors信息，若无，则继续与数据库中数据进行判断
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html", {"username": user.username})
                else:
                    return render(request, "login.html", {"msg": u"用户未激活！"})
            else:
                return render(request, "login.html", {"msg": u"用户名或密码错误！"})
        else:
            return render(request,'login.html', {"login_form":login_form})


class ForgetView(View):
    def get(self,request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html',{"forget_form":forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            if UserProfile.objects.filter(email=email):
                render(request, "forgetpwd.html", {"msg": "邮箱不存在！"})
            send_rigister_email(email,"forget")
            return render(request, "send_susses.html")

        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})


class ResetView(View):
    def get(self,request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email": email})
        else:
            return render(request, "reset_failed.html", {})

    def post(self,request,reset_code):
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        email = request.POST.get("email","")
        modify_form = ModifypwdForm(request.POST)
        if modify_form.is_valid():
            if password1 != password2:
                return render(request, "password_reset.html", {"email": email,"msg": "密码不一致!"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(password2)
            user.save()
            return redirect("login")
        else:
            return render(request, "password_reset.html", {"email": email,"modify_form": modify_form})

