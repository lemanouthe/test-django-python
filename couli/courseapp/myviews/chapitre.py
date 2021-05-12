from django.shortcuts import render, get_object_or_404
from courseapp import models
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import JsonResponse


@login_required(login_url='login')
def addChapitre(request, slug):
    cours = get_object_or_404(models.Cours, slug=slug)
    datas = {
        'cours': cours,
    }
    return render(request,'pages/add-chapitre.html', datas)

class ChapitreDetailView(DetailView):
    context_object_name = 'detail'
    template_name = 'pages/course-chapitre.html'
    
    def get_queryset(self):
        return models.Cours.objects.filter(status=True)
    
    def get_slug_field(self):
        return 'slug'


@csrf_exempt
def post_chapitre(request):
    message, success, url = '', False, ''
    titre = request.POST.get('titre_cour')
    description = request.POST.get('description')
    cours = get_object_or_404(models.Cours, slug=request.POST.get('cours'))

    if not titre:
        message = 'Veuillez entrer un titre'
    elif not description:
        message = 'Veuillez entrer une description'
    else:
        chapitre = models.Chapitre()
        chapitre.cours = cours
        chapitre.titre = titre
        chapitre.description = description
        chapitre.save()
        
        message, success, url = "Enregistrement effectué", True, reverse('cours', kwargs={'slug': cours.slug})

    datas = {
        'message': message,
        'success': success,
        'url': url,
    }

    return JsonResponse(datas, safe=False)