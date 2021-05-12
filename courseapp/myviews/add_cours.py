from django.shortcuts import render, get_object_or_404
from courseapp import models
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.utils import timezone
import json
import re , filetype

@login_required(login_url='login')
def addCours(request):

    datas = {
    }
    return render(request,'pages/add-course.html', datas)

@csrf_exempt
def post_cour_view(request):
    message, success, url = '', False, ''
    titre = request.POST.get('titre_cour')
    description = request.POST.get('description')
    image = request.FILES.get("file")
    prof = get_object_or_404(models.Foramteur, user=request.user)
    kind = filetype.guess(image)
    fichier = ['jpg', 'png']

    if not titre:
        message = 'Veuillez entrer un titre'
    elif not description:
        message = 'Veuillez entrer une description'
    elif not kind.extension in fichier:
        message = "Type de fichier non prise en charge"
    else:
        cour = models.Cours()
        cour.prof = prof
        cour.titre = titre
        cour.description = description
        cour.image = image
        cour.publication = timezone.now()
        cour.save()
        
        message, success, url = "Enregistrement effectué", True, reverse('dashbord', kwargs={})

    datas = {
        'message': message,
        'success': success,
        'url': url,
    }

    return JsonResponse(datas, safe=False)