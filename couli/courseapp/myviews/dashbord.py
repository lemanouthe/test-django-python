from django.shortcuts import render, get_object_or_404
from courseapp import models
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashbord(request):
    prof = get_object_or_404(models.Foramteur, user=request.user)
    cours = models.Cours.objects.filter(status=True, prof=prof).order_by('-date_add')

    datas = {
        'cours': cours,
    }
    return render(request,'pages/profil.html', datas)