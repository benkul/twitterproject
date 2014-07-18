import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tacograbber.settings')
    from grabber.models import Current_Bot, Bot
    newtarget = raw_input("enter current bot: ")
    Current_Bot.user = Bot.objects.get(bot_name=newtarget)


    print Current_Bot.user