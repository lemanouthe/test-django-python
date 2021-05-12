from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
# Register your models here.

class ForamteurAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user',
        'status',
        'date_add',
    )
    

class CoursAdmin(admin.ModelAdmin):

    list_display = (
        'img',
        'titre',
        'prof',
        'publication',
        
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'prof',
        'status',
        'date_add',
    )
    
    def img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="height:80px; width:120px">')
        else:
            return 'Aucun fichier'

    img.short_description = "Prévisualisation"

class ChapitreAdmin(admin.ModelAdmin):

    list_display = (
        'cours',
        'titre',
        
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'cours',
        'status',
        'date_add',
    )

def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Foramteur, ForamteurAdmin)
_register(models.Cours, CoursAdmin)
_register(models.Chapitre, ChapitreAdmin)