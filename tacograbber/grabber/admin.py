from django.contrib import admin
from grabber.models import Category, Page, Bot, Music_Seed, Movie_Seed, Sports_Seed, Current_Bot, UserProfile
from twython_django_oauth.models import TwitterProfile

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Bot)
admin.site.register(Music_Seed)
admin.site.register(Movie_Seed)
admin.site.register(Sports_Seed)
admin.site.register(Current_Bot)
admin.site.register(UserProfile)