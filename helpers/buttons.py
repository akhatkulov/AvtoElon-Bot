from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

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

def post_yes_no():
    x = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text='Ha✅',callback_data="post_yes")
    btn2 = InlineKeyboardButton(text="Yo'q❌",callback_data="post_no")
    x.add(btn1,btn2)
    return x

def admin_yes_no():
    x = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text="Ha✅",callback_data="yes_admin")
    btn2 = InlineKeyboardButton(text="Yo'q❌",callback_data="no_admin")
    x.add(btn1,btn2)
    return x