from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# def home(request):
#     return render(request, 'home.html', {})


def user_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'User name taken')
                return redirect('user_register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('user_register')
            else:
                user = User.objects.create_user(username=user_name, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()

        else:
            messages.info(request, 'Password not matching')
            return redirect('user_register')
        return redirect('/')

    else:
        return render(request, 'accounts/user_register.html')
    # return HttpResponse("Employee index")


def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'product/product_manage_dashboard.html', {})


def logout(request):
    auth.logout(request)
    return redirect("/")


def password_reset(request):
    return render(request, 'accounts/password_reset.html')
