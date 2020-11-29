import os
import json
from forward_ranker import get_mail
# import time
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Sber_mail.models import SberMail
from Sber_mail.serializers import SberMailSerializer, SberMailListSerializer

# Create your views here.
@csrf_exempt
def update(request):
    if request.method == 'GET':
        os.system("python mail_processor.py")
        mails = SberMail.objects.filter(seen=False)
        serializer = SberMailListSerializer(mails, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=503)

@csrf_exempt
def mail_list(request):
    if request.method == 'GET':
        mails = SberMail.objects.filter(seen=False)
        serializer = SberMailListSerializer(mails, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SberMailSerializer(data=data)
        print(data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=503)

@csrf_exempt
def mail_list_priority(request, priority):
    if request.method == 'GET':
        mails = SberMail.objects.filter(seen=False, priority=priority)
        serializer = SberMailListSerializer(mails, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=503)

@csrf_exempt
def mail_detail(request, pk, priority):
    mail = get_object_or_404(SberMail, id=pk)

    if request.method == 'GET':
        serializer = SberMailSerializer(mail)
        mail.seen = True
        mail.save()
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SberMailSerializer(mail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        mail.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=503)

@csrf_exempt
def mail_unsee(request, pk):
    mail = get_object_or_404(SberMail, id=pk)
    if request.method == 'GET':
        mail.seen = False
        mail.save()
        serializer = SberMailSerializer(mail)
        return JsonResponse(serializer.data)
    else:
        return HttpResponse(status=503)

@csrf_exempt
def forwardlist(request, pk):
    mail = get_object_or_404(SberMail, id=pk)
    if request.method == 'GET':
        data_to_send = get_mail(mail.text)
        list = json.dumps(data_to_send)
        print(list)
        return JsonResponse(list, safe=False)
    else:
        return HttpResponse(status=503)

