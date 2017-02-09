from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json
import os
# Create your views here.



ACCESS_TOKEN = os.environ['access']

def index(request):
    pass

def reply(user_id, msg):
    headers = {'Content-type': 'application/json'}
    reply = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, data=json.dumps(reply),headers=headers)
    print(resp.content)


@csrf_exempt
def webhook(request):
  #  temp = request.GET['hub.challenge']

  #  return HttpResponse(temp) 최초 앱을 검증할때
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

    sender = data['entry'][0]['messaging'][0]['sender']['id']
    try:
        message = data['entry'][0]['messaging'][0]['message']['text']
       
        reply(sender, message[::-1])
    except:
        delivery = data['entry'][0]['messaging'][0]['delivery']['seq']
    
    return HttpResponse("ok")