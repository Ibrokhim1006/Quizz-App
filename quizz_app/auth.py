from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group,User
from django.contrib.auth .decorators import login_required

def sigin_in(request):
    context = {}
    username = request.POST.get('username',False)
    password = request.POST.get('password')
    if username=='' or password=='':
        context['error'] = "Вы не ввели логин или пароль !"
        return render(request,'authorization/sigin_in.html',context)
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('home_personal')  
    else:
        context['error']='Hеверный логин или пароль !'
    return render(request,'authorization/sigin_in.html',context)

def sigin_up(request):
    context = {}
    if request.method=='POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password_1 = request.POST.get('password_1')
        if username=='' or first_name=='' or last_name=='' or password=='' or password_1=='':
            context['error'] = "Заполните информацию"
            return render(request,'authorization/sigin_up.html',context)
        user_name = User.objects.filter(username=username)
        if len(user_name)!=0:
            context['error'] = "Такой логин уже зарегистрирован !"
            return render(request,'authorization/sigin_up.html',context)
        if password!=password_1:
            context['error'] = "Перепроверьте пароль"
            return render(request,'authorization/sigin_up.html',context)
        my_user = User.objects.create(username=username,first_name=first_name,last_name=last_name)
        my_user.set_password(password)
        my_user.save()
        return redirect('sigin_in')
    return render(request,'authorization/sigin_up.html',context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('sigin_in')