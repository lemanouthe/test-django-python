from django.urls import path
from .myviews import login, index, chapitre


urlpatterns = [
    path('', login.login_view, name='login'),
    path('index', index.index, name='index'),
    path('cours', chapitre.chapitre, name='cours'),
    path('chapitre/<slug:slug>', chapitre.ChapitreDetailView.as_view(), name='chapitre'),
    
]