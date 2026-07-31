from django.shortcuts import render
from .models import *

def index(request):
    izohlar = Izohlar.objects.all()[:3]
    twohund = Twohundered.objects.all()
    projects = MyProject.objects.all()
    ctx = {
        'comment': izohlar,
        'two' : twohund,
        'projects' : projects,
    }
    return render(request,'index.html', ctx)