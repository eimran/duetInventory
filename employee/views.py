from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'employee/employee_profile.html')
    # return HttpResponse("Employee index")


def register(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    # djtext = request.GET.get('text', 'default')

    params = {'result': res}
    return render(request, 'employee/after_registration.html', params)


    #return HttpResponse("Employee index")
