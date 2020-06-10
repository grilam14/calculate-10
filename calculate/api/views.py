from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from calculate.api.models import Numbers
import json
from datetime import datetime

from django.core import serializers

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def add_number(request):
    number = request.POST['number']
    Numbers.objects.create(number=number)

    query = Numbers.objects.all().order_by('-time').values('number', 'time')[:10]

    return HttpResponse("Success")

def get_numbers(request):
    query = Numbers.objects.all().order_by('-time').values('number', 'time')[:10]
    for obj in query:
        obj['time'] = str(obj['time'].strftime('%Y-%m-%d %H:%M'))

    query_json = json.dumps(list(query))
    context = {'numbers': query_json}
    return JsonResponse(context)