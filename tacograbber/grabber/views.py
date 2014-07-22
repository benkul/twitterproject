# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from grabber.models import Bot, Current_Bot
from grabber.forms import CreateTweet, BotTokenForm
from twython import Twython, TwythonError

# standing global for current_bot
yellow = ""

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
    if request.method == 'POST':
        form = BotTokenForm(request.POST)
        if form.is_valid():
            global yellow
            yellow = Bot.objects.get(id=request.POST.get('user'))
            return begin_auth(request)
        else:
            print form.errors
    else:
        form = BotTokenForm()


    return render_to_response('grabber/generate.html',{'form': form}, context)

def get_tokens(request):
    context = RequestContext(request)
    context_dict = {'thank_you_message' : "Tokens arrived on time!"}
    return render_to_response('grabber/index.html', context_dict, context)


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
            message = request.POST.get('tweeted')

            tweeter = Bot.objects.get(id=request.POST.get('user'))

            twitter = Twython(tweeter.api, tweeter.api_secret,
                      tweeter.oauth_token, tweeter.oauth_secret)
            try:
                twitter.update_status(status=message)
            except TwythonError as e:
                print e
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





from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.urlresolvers import reverse
from grabber.models import Current_Bot, Bot
from twython import Twython

User = get_user_model()


# If you've got your own Profile setup, see the note in the models file
# about adapting this to your own setup.
from twython_django_oauth.models import TwitterProfile


def logout(request, redirect_url=settings.LOGOUT_REDIRECT_URL):
    """
        Nothing hilariously hidden here, logs a user out. Strip this out if your
        application already has hooks to handle this.
    """
    django_logout(request)
    return HttpResponseRedirect(request.build_absolute_uri(redirect_url))


def begin_auth(request):
    """The view function that initiates the entire handshake.

    For the most part, this is 100% drag and drop.
    """
    # Instantiate Twython with the first leg of our trip.
    twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET)

    # Request an authorization url to send the user to...
    callback_url = request.build_absolute_uri(reverse('twython_django_oauth.views.thanks'))
    auth_props = twitter.get_authentication_tokens(callback_url)

    # Then send them over there, durh.
    request.session['request_token'] = auth_props
    return HttpResponseRedirect(auth_props['auth_url'])


def thanks(request, redirect_url=settings.LOGIN_REDIRECT_URL):
    """A user gets redirected here after hitting Twitter and authorizing your app to use their data.

    This is the view that stores the tokens you want
    for querying data. Pay attention to this.

    """
    # Now that we've got the magic tokens back from Twitter, we need to exchange
    # for permanent ones and store them...
    oauth_token = request.session['request_token']['oauth_token']
    oauth_token_secret = request.session['request_token']['oauth_token_secret']
    twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET,
                      oauth_token, oauth_token_secret)

    # Retrieve the tokens we want...
    authorized_tokens = twitter.get_authorized_tokens(request.GET['oauth_verifier'])
    global yellow
    #weeter = Bot.objects.get(bot_name="emilyquark")


    yellow.oauth_token = authorized_tokens['oauth_token']
    yellow.user.oauth_secret = authorized_tokens['oauth_token_secret']
    yellow.user.save()
    print yellow.oauth_token, yellow.oauth_secret

    # If they already exist, grab them, login and redirect to a page displaying stuff.
    #try:
    #    user = User.objects.get(username=authorized_tokens['screen_name'])
    #except User.DoesNotExist:
        # We mock a creation here; no email, password is just the token, etc.
    #    user = User.objects.create_user(authorized_tokens['screen_name'], "fjdsfn@jfndjfn.com", authorized_tokens['oauth_token_secret'])
    #    profile = TwitterProfile()
    #    profile.user = user
    #    profile.oauth_token = authorized_tokens['oauth_token']
    #    profile.oauth_secret = authorized_tokens['oauth_token_secret']
    #    profile.save()

    #user = authenticate(
    #    username=authorized_tokens['screen_name'],
    #    password=authorized_tokens['oauth_token_secret']
    #)
    #login(request, user)
    return HttpResponseRedirect(redirect_url)


def user_timeline(request):
    """An example view with Twython/OAuth hooks/calls to fetch data about the user in question."""
    user = request.user.twitterprofile
    twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET,
                      Current_Bot.user.oauth_token, Current_Bot.user.oauth_secret)
    user_tweets = twitter.get_home_timeline()
    return render_to_response('tweets.html', {'tweets': user_tweets})

def twitter_return(request):
    return render_to_response('grabber/index.html')
