from django.shortcuts import render
from Battlefield.factory import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def result(request):
    if request.POST['armies_num']:
        armies_num = int(request.POST['armies_num'])
    else:
        armies_num = 2

    factory = Factory()
    battlefield = factory.create_battlefield(armies_num)
    res = battlefield.start()
    return render(request, 'result.html', {'res': res})
