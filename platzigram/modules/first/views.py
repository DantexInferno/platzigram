import json
from django.http.response import HttpResponse
from datetime import datetime

def hello_world(request):
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
  return HttpResponse(f"current serve time {now}")

def hi(request, name, age):
  if age < 12:
    message = f"Sorry {name}, Your age must be higher than 12 and your age is {age}"
  else:
    message = f"hellow {name} Welcome to Platzigram"
      
  return HttpResponse(message)