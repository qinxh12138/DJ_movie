from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login_test(request):
    if request.method == 'GET':
        return render(request, 'login.htm', {'msg': "请输入正确的格式"})
    elif request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.htm', {'msg': "用户不存在"})
        except:
            return render(request, 'login.htm', {'msg': "参数错误"})
    else:
        return render(request, 'login.htm', {'msg': "请求错误"})


def register_test(request):
    if request.method == 'GET':
        # return_url = request.GET.get('next')
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # return_url = request.POST.get('next')
        user = authenticate(request, username=username)
        if user:
            render(request, 'login.htm', {'msg': "该用户已经存在,请直接登录"})
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            # if return_url:
            #     return redirect(return_url)
            # else:
            return redirect('/')


@login_required
def logout_test(request):
    logout(request)
    return redirect('/')
