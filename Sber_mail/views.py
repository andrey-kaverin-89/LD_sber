import os
# import time
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Sber_mail.models import SberMail
from Sber_mail.serializers import SberMailSerializer

# Create your views here.
@csrf_exempt
def update(request):
    if request.method == 'GET':
        os.system("python mail_processor.py")
        mails = SberMail.objects.filter(seen=False)
        serializer = SberMailSerializer(mails, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=503)

@csrf_exempt
def mail_list(request):
    if request.method == 'GET':
        mails = SberMail.objects.filter(seen=False)
        serializer = SberMailSerializer(mails, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SberMailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def mail_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    # try:
    #     mail = SberMail.objects.get(pk=pk)
    #     mail[-1].seen = True
    #     mail[-1].save()
    # except SberMail.DoesNotExist:
    #     return HttpResponse(status=404)
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