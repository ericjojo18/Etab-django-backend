from typing import Any
from django.shortcuts import redirect
from django.urls import reverse

class RedirectAuthenticateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request) :
        # Vérifie si l'utilisateur est authentifié et essaie d'accéder à la page de connexion
        if request.user.is_authenticated and request.path == reverse('auth:login'):
            return redirect("/dashbord")  # Remplacez 'home' par l'URL souhaitée

        response = self.get_response(request)
        return response
        