from display import models
from django.http import HttpResponse, JsonResponse
import csv
from io import TextIOWrapper
from . import models
import json

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
        return JsonResponse({"message":"Failed"},status=404)
    
def preferenceUpload(request):
    if request.method == 'POST':
        interval = request.POST.get('interval')
        uploaded_file = request.FILES.get('file')
        user = models.User.objects.get(id=request.id)
        
        if uploaded_file:
            # Assuming the uploaded file is a CSV file
            try:
                # Wrap the uploaded file in TextIOWrapper to handle CSV reading
                csv_file = TextIOWrapper(uploaded_file.file, encoding='utf-8')

                # Create a CSV reader
                csv_reader = csv.reader(csv_file)

                # Iterate through the rows in the CSV file
                for row in csv_reader:
                    # 'row' is a list representing each row in the CSV file
                    new = models.userSymbols(
                        user = models.User(id=request.user),
                        symbol = models.Symbol(id=row[0])
                    )
                    new.save()
                # If you want to process the rows further, you can do it here

                return HttpResponse("CSV file processed successfully")
            except Exception as e:
                return HttpResponse("Error processing CSV file: " + str(e))

        return HttpResponse("No file uploaded")

    return HttpResponse("Invalid request method")