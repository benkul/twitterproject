from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(max_length=128)
    bot = models.ForeignKey('Bot')

    def __unicode__(self):
        return self.title


class Bot(models.Model):
    name = models.CharField(max_length=128, unique=True)
    email = models.CharField(max_length=128)
    email_secret = models.CharField(max_length=128)
    dob = models.DateField()
    api = models.CharField(max_length=128)
    api_secret = models.CharField(max_length=128)
    oauth_token = models.CharField(max_length=128)
    oauth_secret = models.CharField(max_length=128)
    bot_name = models.CharField(max_length=128) #twitterhandle
    movie_seed = models.ForeignKey('Movie_Seed')
    music_seed = models.ForeignKey('Music_Seed')
    sports_seed = models.ForeignKey('Sports_Seed')

    def see_movies(self):
        movie_string = "%s, %s, %s" % (self.movie_seed.movie1, self.movie_seed.movie2, self.movie_seed.movie3)
        return movie_string

    def see_music(self):
        music_string = "%s, %s, %s" % (self.music_seed.music1, self.music_seed.music2, self.music_seed.music3)
        return music_string

    def see_sports(self):
        sports_string = "%s, %s, %s" % (self.sports_seed.sport1, self.sports_seed.sport2, self.sports_seed.sport3)
        return sports_string


    def __unicode__(self):
        return self.name

class Current_Bot(models.Model):
    user = models.ForeignKey('Bot')
    

    def __unicode__(self):
        return self.user.bot_name

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class Movie_Seed(models.Model):
    name = models.CharField(max_length=128, unique=True) #name of bot using seed
    movie1 = models.CharField(max_length=128)
    movie2 = models.CharField(max_length=128)
    movie3 = models.CharField(max_length=128)




    def __unicode__(self):
        return self.name

class Music_Seed(models.Model):
    name = models.CharField(max_length=128, unique=True) #name of bot using seed
    music1 = models.CharField(max_length=128)
    music2 = models.CharField(max_length=128)
    music3 = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Sports_Seed(models.Model):
    name = models.CharField(max_length=128, unique=True) #name of bot using seed
    sport1 = models.CharField(max_length=128)
    sport2 = models.CharField(max_length=128)
    sport3 = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name