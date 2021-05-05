import telebot
from datetime import datetime
import time
from threading import Thread
f=0
#-1001496381625
def timer(h: int, m: int):
    now = datetime.today()
    date=datetime.timetuple(datetime.now())
    NY = datetime(date.tm_year, date.tm_mon, date.tm_mday, h, m)
    d = NY-now
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    if hh>1:
        return("Тренировка началась, а кто-то как обычно опаздает👍")
    hh=str(hh)
    mm=str(mm)
    ss=str(ss)
    if len(hh)==1:
        hh="0"+hh
    if len(mm)==1:
        mm="0"+mm
    if len(ss)==1:
        ss="0"+ss
    return "{}:{}".format(hh, mm)
bot = telebot.TeleBot('')
def editor(message):
    while True:
        mid=message.message_id
        time.sleep(5)
        a=str(timer(18, 0))
        try:
            if a.find("Тренировка началась")!=-1:
                bot.edit_message_text(chat_id=message.chat.id, message_id=mid, text=f"{a}")
                break
            else:
                bot.edit_message_text(chat_id=message.chat.id, message_id=mid, text=f"Осталось {a} до трентровки")
        except Exception as e:
            e=str(e)
            if e.find("message to edit not found")!=-1:
               mid = (bot.send_message(-1001496381625, f"Осталось {a} до трентровки")).message_id
def sender():
    global f
    f=0
    while True:
        now = str(datetime.now())
        now = (now[now.find(" ")+1:now.find(" ")+6])
        day = datetime.now().weekday()
        a=str(timer(18,0))
        if (f==0 and now=="17:00") and (day==0 or day==2 or day==4):
            msg = bot.send_message(-1001496381625, f"Осталось {a} до трентровки")
            Thread(target=editor, args=(msg,)).start()
            f=1
        elif now!="17:00":
        	f=0
        time.sleep(5)
sender()
@bot.message_handler(commands=['id'])
def send_welcome(message):
	bot.send_message(message.chat.id, str(message.chat.id))
bot.polling(none_stop=True)