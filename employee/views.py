from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'employee/employee_profile.html')
    # return HttpResponse("Employee index")
