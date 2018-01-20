from django.http import JsonResponse
from django.contrib.auth import authenticate
from .models import UserProfile
from core.decorators import token_required
import jwt
import json
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

SECRET_KEY = settings.SECRET_KEY


def login_view(request):
    req_data = json.loads(request.body.decode('utf-8'))
    username = req_data['username']
    password = req_data['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse(
            {"error": "Incorrect username/password combination"},
            status=400
        )
    else:
        token = jwt.encode({'user_id': user.id}, SECRET_KEY)
        return JsonResponse({'token': token.decode("utf-8")})


def signup_view(request):
    req_data = json.loads(request.body.decode('utf-8'))
    username = req_data['username']
    password = req_data['password']
    firstname = req_data['first_name']
    country_name = req_data['country_name']
    try:
        user = User.objects.create_user(username=username,
                                        password=password,
                                        first_name=firstname)
        userprofile = UserProfile(user=user, country_name=country_name)
        userprofile.save()
        token = jwt.encode({'user_id': user.id}, SECRET_KEY)
        return JsonResponse({'token': token.decode("utf-8")})
    except Exception:
        return JsonResponse({'error':
                            "username is already exist in the database"})


@token_required
def hello_view(request):
    return JsonResponse({"hello": "world"})
