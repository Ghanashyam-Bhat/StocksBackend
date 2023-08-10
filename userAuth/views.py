from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from display import models as display

# Create your views here.
def login_api(request):    
    req_body = request.body.decode('utf-8')
    req = json.loads(req_body)
    email = req["email"]
    password = req["password"]
    user = authenticate(request, username=email, password=password)

    if user is not None:
        # Authentication successful
        login(request, user)        
        response =  JsonResponse({'message': 'SUCCESS'}, status=201)
        return response   
    else:
        # Authentication failed
        return JsonResponse({'message': 'FAILURE'}, status=401)


def signup_api(request):
    req_body = request.body.decode('utf-8')
    req = json.loads(req_body)
    email = req["email"]
    password = req["password"]
    user = User.objects.filter(username=email).first()
    if user:
        response = JsonResponse({'message': 'USER ALREADY EXISTS WITH THE GIVEN EMAIL'}, status=302)
    try:
        # Create a new user
        user = User.objects.create_user(username=email, password=password)
        new = display.User(id=email)
        new.save()
        response =  JsonResponse({'message': 'SUCCESS'}, status=201)
        return response   
    except Exception as e:
        # Handle any exceptions that occur during user creation or group addition
        print(f"An error occurred: {str(e)}")
        response = JsonResponse({'message': 'FAILURE'}, status=500)
        return response 

def logout_api(request):
    if not request.user.is_authenticated:
        response =  JsonResponse({'message': 'REDIRECT'}, status=302)
        return response
    try:
        logout(request)
        response =  JsonResponse({'message': 'SUCCESS'}, status=201)
        return response
    except:
        response = JsonResponse({'message': 'FAILURE'}, status=401)
        return response