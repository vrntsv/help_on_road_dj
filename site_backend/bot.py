import telebot
from . import models
BOT_TOKEN = ['-']

bot = telebot.TeleBot(BOT_TOKEN[0])


def send_message_tech(text, city_list, image=None, to_all=False, to_excl=False, to_clients=False, temp=False):
    emp_ids = None
    if not city_list:
        city_list = []
        city_dict = models.Employees.objects.values('id')
        for city in city_dict:
            city_list.append(city['id'])
    print(city_list)
    if to_all:
        emp_ids = models.Employees.objects.filter(id_city__in=list(city_list)).values('id')
    elif to_excl:
        emp_ids = models.Employees.objects.filter(exclusive=1, id_city__in=list(city_list)).values('id')
    elif to_clients:
        emp_ids = models.Client.objects.all().values('id')
    print(emp_ids)
    for id in emp_ids:
        try:
            if image and image != '':
                msg = bot.send_photo(chat_id=id['id'], photo=image, caption=text)
            else:
                msg = bot.send_message(chat_id=id['id'], text=text)
            if temp and temp != '':
                message_to_save = models.Messages(id=msg.message_id, id_user=id['id'])
                message_to_save.save()
        except:
            print('err sending to {}'.format(id['id']))

