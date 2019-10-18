from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    import datetime

    template = loader.get_template("app/index.html")
    context = {"hoje": datetime.datetime.now()}
    return HttpResponse(template.render(context, request))


def ping2(request):
    return HttpResponse('PONG!')
