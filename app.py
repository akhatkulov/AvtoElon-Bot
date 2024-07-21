from telebot import TeleBot, types
from PIL import Image
from io import BytesIO
import json
from telegraph import Telegraph

from helpers.buttons import home_menu, ads_yes_no,post_yes_no,admin_yes_no
from helpers.alch import create_user, put_step, get_step,change_info,get_info
from helpers.others import step_msg,steps

bot = TeleBot(token="5790375885:AAHKyTQ6T7vbPuYVAijxCMtdXm1_bFHRmno")
telegraph = Telegraph()
rek_text = " "
# Create a Telegraph account
response = telegraph.create_account(short_name='my_bot')
access_token = response['access_token']
# A dictionary to store user-specific image paths
user_images = {}

@bot.message_handler(commands=['start'])
def home(msg: types.Message):
    try:
        create_user(cid=msg.chat.id)
    except:
        pass
    bot.send_message(chat_id=msg.chat.id, text="Salom botga hush kelibsiz", reply_markup=home_menu())
    put_step(cid=msg.chat.id,step="0")

@bot.callback_query_handler(func=lambda call: True)
def get_ads(call):
    if call.data == "put_ads":
        print("-----")
        bot.send_message(chat_id=call.message.chat.id, text="E'lon joylamoqchimisiz?", reply_markup=ads_yes_no())
    elif call.data == "yes_ads":
        bot.send_message(chat_id=call.message.chat.id, text="Mashinaning 4ta rasmini yuboring")
        put_step(cid=call.message.chat.id, step="get_photos")
        user_images[call.message.chat.id] = []

@bot.message_handler(content_types=['photo', 'text'])
def main_funks(msg: types.Message):
    text = msg.text
    cid = msg.chat.id
    step = get_step(cid=cid)
    
    if step == "get_photos":
        if cid not in user_images:
            user_images[cid] = []

        if msg.photo:
            try:
                # Get file info and download the photo
                file_info = bot.get_file(msg.photo[-1].file_id)
                file = bot.download_file(file_info.file_path)
                image = Image.open(BytesIO(file))

                # Convert the image to bytes
                byte_io = BytesIO()
                image.save(byte_io, format='JPEG')
                byte_io.seek(0)
                photo_bytes = byte_io.read()

                # Upload the image to Telegraph
                with open('temp.jpg', 'wb') as temp_file:
                    temp_file.write(photo_bytes)

                response = telegraph.upload_file('temp.jpg')
                image_url = 'https://telegra.ph/' + response[0]['src']
                print(image_url)

                # Save the image URL
                user_images[cid].append(image_url)

                # Check if 4 images are collected
                if len(user_images[cid]) == 4 or msg.text == "STOP":
                    img_x = json.dumps(user_images[cid])
                    print(img_x)
                    change_info(cid=cid, type_info="pic", value=img_x)
                    bot.send_message(chat_id=msg.chat.id, text="""<b>Rasmlarni yuklash yakunlandi!
Avtomobile modelini yuboring!
Masalan:</b> <i>(Spark 2-pozitsiya sotiladi)</i>""", parse_mode="html")
                    put_step(cid=msg.chat.id, step="name")
                    user_images[cid] = []  # Reset the list after sending

            except Exception as e:
                print(f"Error: {e}")
    print(step)
    if step == "km":

        main_info = get_info(cid=cid)
        x = main_info
        pic = json.loads(x['pic'])
        rasm = pic
        model = x["name"]
        sana = x["year"]
        km = x['km']
        gas = x['oil']
        texnik = x['is_clear']
        narx = x['cost']
        manzil = x['location']
        kraska = x['color']
        nomer = x['phone']
            
        text_info = f"""
<b>🚗| {model} </b>

<i>📆Yili: {sana}
🚦Km: {km}
⛽️Yoqilg'i: {gas}
🛠Texnik holati: {texnik}
🎨Kraska: {kraska}
<b>💰Narxi: {narx}

📍Manzil: {manzil}</b>

📞Nomer: {nomer}

{rek_text}
"""
        media = [types.InputMediaPhoto(media=pic_url, caption=text_info if i == 0 else '', parse_mode='HTML') for i, pic_url in enumerate(rasm)]
        bot.send_media_group(chat_id=cid, media=media)
        bot.send_message(chat_id=cid,text="Ushbu anketa to'grimi?",reply_markup=post_yes_no())
        
    elif step in steps:
        change_info(cid=cid, type_info=step, value=text)
        x_index = steps.index(step)
        bot.send_message(cid, step_msg[steps[x_index + 1]], parse_mode="html")
        put_step(cid=cid, step=steps[x_index + 1])

print(bot.get_me())
bot.polling()
