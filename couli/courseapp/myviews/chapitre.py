from django.shortcuts import render
from courseapp import models
from django.views.generic.detail import DetailView


def chapitre(request, slug):
    chapitres = models.Chapitre.objects.filter(status=True, cours__slug=slug)
    
    datas = {
        'chapitres': chapitres
    }
    return render(request,'pages/siteweb/index.html', datas)

class ChapitreDetailView(DetailView):
    context_object_name = 'chapitre'
    template_name = ''
    
    def get_queryset(self):
        return models.Chapitre.objects.filter(status=True)
    
    def get_slug_field(self):
        return 'titre_slug'

# def detail(request, slug):
    
#     chapitre = models.Chapitre.objects.get(slug=slug)
    
#     datas = {
#         'chapitre': chapitre
#     }
#     return render(request,'pages/siteweb/index.html', datas)