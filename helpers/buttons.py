from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

def home_menu():
    x = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text="Kanalga e'lon joylash",callback_data="put_ads")
    btn2 = InlineKeyboardButton(text="Biz haqimizda",callback_data="our_info")
    btn3 = InlineKeyboardButton(text="Qo'llanma",callback_data="guide")
    x.add(btn1)
    x.add(btn2,btn3)
    return x

def ads_yes_no():
    x = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text="Ha✅",callback_data="yes_ads")
    btn2 = InlineKeyboardButton(text="Yo'q❌",callback_data="no_ads")
    x.add(btn1,btn2)
    return x

def post_yes_no(uid):
    x = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text='Ha✅',callback_data=f"yes-post_{uid}")
    btn2 = InlineKeyboardButton(text="Yo'q❌",callback_data=f"no-post_{uid}")
    x.add(btn1,btn2)
    return x

def admin_yes_no(uid,cid):
    x = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text="Ha✅",callback_data=f"yes-admin_{uid}_{cid}")
    btn2 = InlineKeyboardButton(text="Yo'q❌",callback_data=f"no-admin_{uid}_{cid}")
    x.add(btn1,btn2)
    return x

def skip():
    x = ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    btn1 = KeyboardButton("Tasdiqlash ✅")
    x.add(btn1)
    return x

def keyboard_rm():
    markup = ReplyKeyboardRemove()
    return markup