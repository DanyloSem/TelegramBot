from tbot_base.bot import tbot as bot
from tbot.models import TelegramUser

def send_news_to_users(news_title, news_content):
    users = TelegramUser.objects.all()

    for user in users:
        message = f'New news: {news_title}\n\n{news_content}'
        bot.send_message(user.user_id, message)