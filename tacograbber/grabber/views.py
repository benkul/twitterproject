# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from grabber.models import Bot, Current_Bot
from grabber.forms import CreateTweet


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


    return render_to_response('grabber/botprofile.html',context_dict, context)


def create_tweet(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = CreateTweet(request.POST)
        if form.is_valid():
            form.save(commit=True)
            message = request.POST.get('tweeted')
            currently_tweeting = request.POST.get('user')
            print message
            print currently_tweeting
            return post_tweet(request)
        else:
            print form.errors
    else:
        form = CreateTweet()
    return render_to_response('grabber/index.html',{'form': form}, context)

def post_tweet(request):
    context = RequestContext(request)
    context_dict = {'thank_you_message' : "Thank you for tweeting"}
    return render_to_response('grabber/index.html', context_dict, context)