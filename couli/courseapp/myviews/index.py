from django.shortcuts import render
from courseapp import models


def index(request):
    recent = models.Cours.objects.filter(status=True).order_by('publication')[:3]

    datas = {
        'recent': recent,
    }
    return render(request,'pages/siteweb/index.html', datas)