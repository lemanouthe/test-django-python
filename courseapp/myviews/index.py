from django.shortcuts import render
from courseapp import models
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    recent = models.Cours.objects.filter(status=True).order_by('-date_add')[:3]

    datas = {
        'recent': recent,
    }
    return render(request,'pages/index.html', datas)