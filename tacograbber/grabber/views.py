# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from grabber.models import Bot


def index(request):
    context = RequestContext(request)
    return render_to_response('grabber/index.html', context)


def about(request):
    context = RequestContext(request)
    bot_list = Bot.objects.order_by('-name')
    context_dict = {'bots': bot_list}
    return render_to_response('grabber/about.html', context_dict, context)


def generate(request):
    context = RequestContext(request)
    return render_to_response('grabber/generate.html', context)

def bot_profile(request, bot_name):
    context = RequestContext(request)
    bot = Bot.objects.get(bot_name=bot_name)
    context_dict = {"bot" : bot}

    return render_to_response('grabber/botprofile.html', context_dict, context)