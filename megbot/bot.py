#Создайте виртуальное окружение в папке где находится ваш бот для Телеграмма
#Активируйте виртуальное окружение
#Запустите бота и убедитесь, что python не может импортировать python-telegram-bot
#Установите python-telegram-bot[socks] и убедитесь, что бот запускается
#Добавьте папку виртуального окружения в .gitignore

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start, вы можете вызвать /planet x, заменив x на название планеты'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format (update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def planetarium(bot, update):
    user_text = update.message.text.split()
    print(user_text)
    pl = user_text[1].capitalize()
    print(pl)
    time = ephem.Date(datetime.date.today())
    print(time)
    try:
        planet = getattr(ephem, pl)()
        planet.compute(time)
        res = ephem.constellation(planet)
        update.message.reply_text(f'Сегодня планета {pl} находится в созвездии {res}')
    except (AttributeError, TypeError):
        update.message.reply_text('планета не из нашей вселенной!!')
        


def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)
    logging.info('Бот запускается')

    dp = mybot.dispatcher   # диспетчер получает команду и разкидывает ее по назначению
    dp.add_handler(CommandHandler('start', greet_user))  # команда для вызова нашей функции
    dp.add_handler(CommandHandler('planet', planetarium)) 
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))  
    
    mybot.start_polling() # бот начинает проверять входящие сообщения
    mybot.idle()  # Заставляем бота работать бесконечно

main()
