from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        message, success, url = '', False, ''
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(Q(email=email) | Q(username=email) & Q(is_active=True)).first()
        next = request.POST.get('next')

        if user:
            utilisateur = authenticate(username=user.username, password=password)
            if utilisateur:
                login(request, utilisateur)
                message, success = 'Connexion effectué', True
                if next != 'None':
                    url = next
                else:
                    url = reverse('index', kwargs={})
            else:
                message = 'Vos identifiants ne sont pas correctes.'
        else:
            message = "Vos identifiants n\'existent pas."
        datas = {
            'message': message,
            'success': success,
            'url': url,
        }
        return JsonResponse(datas, safe=False)
    else:
        if request.user.is_authenticated:
            return redirect('index')
        next = request.GET.get('next')
        
        datas = {
            'next': next,
        }
        return render(request,'pages/login.html', datas)

def logout_view(request):
    logout(request)
    return redirect('login')