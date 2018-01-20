from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
import jwt

SECRET_KEY = settings.SECRET_KEY


def token_required(view_func):
    def wrapper(request, *args, **kwargs):
        token = request.META.get('HTTP_X_AUTH_TOKEN', None)
        if token is None:
            return JsonResponse({"error": "token not supplied"}, status=400)
        try:
            token = jwt.decode(token, SECRET_KEY)
            request.swiss_user = User.objects.get(id=token.get('user_id'))
        except jwt.exceptions.InvalidTokenError:
            return JsonResponse({"error": "invalid token"}, status=400)
        return view_func(request, *args, **kwargs)
    return wrapper
