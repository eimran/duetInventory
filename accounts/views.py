from django.shortcuts import render, redirect
from  django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from accounts.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from employee.models import Employee


# def home(request):
#     return render(request, 'home.html', {})

def registration_view(request):

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            employee = form.cleaned_data.get('employee')
            account = authenticate(email=email, password=raw_password, username=username, employee=employee)
            login(request, account)
            return redirect('/')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        # context['registration_form'] = form
        context = {'registration_form': form}
    return render(request, 'accounts/user_register.html', context)


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("dashboard")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    # print(form)
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


# def password_reset(request):
#     return render(request, 'accounts/password_reset.html')

def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "employee": request.user.employee,
                # "password": request.user.password,
            }
        )
    context['account_form'] = form
    return render(request, 'accounts/account.html', context)


def dashboard(request):
    return render(request, 'product/product_manage_dashboard.html', {})

#
# def user_register(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         user_name = request.POST['user_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#
#         if password == confirm_password:
#             if User.objects.filter(username=user_name).exists():
#                 messages.info(request, 'User name taken')
#                 return redirect('user_register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email already taken')
#                 return redirect('user_register')
#             else:
#                 user = User.objects.create_user(username=user_name, password=password, email=email,
#                                                 first_name=first_name, last_name=last_name)
#                 user.save()
#
#         else:
#             messages.info(request, 'Password not matching')
#             return redirect('user_register')
#         return redirect('/')
#
#     else:
#         return render(request, 'accounts/user_register.html')
#     # return HttpResponse("Employee index")
#
#
# def login(request):
#     if request.method == 'POST':
#         user_name = request.POST['user_name']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=user_name, password=password)
#
#         if user is not None:
#             auth.login(request, user)
#             return redirect('dashboard')
#         else:
#             messages.info(request, 'invalid credentials')
#             return redirect('login')
#
#     else:
#         return render(request, 'accounts/login.html')
#
#
# def dashboard(request):
#     return render(request, 'product/product_manage_dashboard.html', {})
#
#
# def logout(request):
#     auth.logout(request)
#     return redirect("/")
#
#
# def password_reset(request):
#     return render(request, 'accounts/password_reset.html')
