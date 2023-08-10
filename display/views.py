from display import models
from django.http import HttpResponse, JsonResponse

# Create your views here.
def preferenceSelection(request):
    username = request.user
    try:
        preferences = models.userSymbols.objects.filter(user__id=username)
        preferList = []
        for prefer in preferences:
            preferList.append(prefer.id)
        return JsonResponse({"list":preferList},status=201)
    except Exception as e:
        return JsonResponse({"messgae":"Failed"},status=404)