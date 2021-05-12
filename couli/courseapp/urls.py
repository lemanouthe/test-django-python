from django.urls import path
from .myviews import login, index, chapitre, dashbord, add_cours


urlpatterns = [
    path('', login.login_view, name='login'),
    path('logout', login.logout_view, name='logout'),
    path('index', index.index, name='index'),
    path('cours/<slug:slug>', chapitre.ChapitreDetailView.as_view(), name='cours'),
    path('dashbord', dashbord.dashbord, name="dashbord"),
    path('add-cours', add_cours.addCours, name="add_cours"),
    path('post-cours', add_cours.post_cour_view, name='post_cours'),
    
    path('add-chapitre/<slug:slug>', chapitre.addChapitre, name="add_chapitre"),
    path('post-chapitre', chapitre.post_chapitre, name='post_chapitre'),
    
    
]