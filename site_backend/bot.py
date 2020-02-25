import telebot
import models

BOT_TOKEN = ['-']

bot = telebot.TeleBot(BOT_TOKEN[0])


def send_message_tech(text, city_list, image=None, to_all=False, to_excl=False, to_clients=False):
    if to_all:
        emp_ids = models.Employees.objects.filter(id_city__in=city_list).values('id')
    elif to_excl:
        emp_ids = models.Employees.objects.filter(exclusive=1, id_city__in=city_list).values('id')
    elif to_clients:
        emp_ids = models.Client.objects.all().values('id')
    print(emp_ids)
    for id in emp_ids:
        try:
            if image:
                bot.send_photo(chat_id=id, photo=image, caption=text)
            else:
                bot.send_message(chat_id=id, text=text)
        except:
            print('err sending to {}'.format(id))

