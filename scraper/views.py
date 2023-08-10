import csv
from io import TextIOWrapper
from django.http import HttpResponse, JsonResponse

# Create your views here.
def preferenceSelection(request):
    if request.method == 'POST':
        req_body = request.POST.get('request')
        uploaded_file = request.FILES.get('file')

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
                    print(row)
                
                # If you want to process the rows further, you can do it here

                return HttpResponse("CSV file processed successfully")
            except Exception as e:
                return HttpResponse("Error processing CSV file: " + str(e))

        return HttpResponse("No file uploaded")

    return HttpResponse("Invalid request method")
    