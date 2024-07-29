from telebot import TeleBot, types
from PIL import Image
from io import BytesIO
import json
from telegraph import Telegraph
from uuid import uuid4
from helpers.buttons import home_menu, ads_yes_no,post_yes_no,admin_yes_no,skip,keyboard_rm
from helpers.alch import create_user, put_step, get_step,change_info,get_info,create_post,get_post
from helpers.others import step_msg,steps

bot = TeleBot(token="BOT_TOKEN") #bot token
telegraph = Telegraph()
rek_text = " " #reklama matni
admin = 789945598 #admin id
channel_id = -1001977042344 #post channel id

response = telegraph.create_account(short_name='my_bot')
access_token = response['access_token']
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
    call_msg = call.message
    chat_id = call_msg.chat.id
    rply = call_msg.reply_to_message
    rply_id = rply.message_id if rply else None

    if call.data == "put_ads":
        print("-----")
        bot.send_message(chat_id=call.message.chat.id, text="E'lon joylamoqchimisiz?", reply_markup=ads_yes_no())
    elif call.data == "yes_ads":
        bot.send_message(chat_id=call.message.chat.id, text="<b>Avtomobilning 1-4 tagacha rasmini yuboring!\nRasmlarni yuborib bo'lgandan keyin quyidagi Tasdiqlash ✅ tugmasini bosing.\nEslatma:</b> <i>Har qanday rasm bo'lmagan kontent uchun e'lon berish to'xtatiladi!</i>",parse_mode="html",reply_markup=skip())
        put_step(cid=call.message.chat.id, step="get_photos")
        user_images[call.message.chat.id] = []
    elif "yes-post" in call.data:
        post_id = call.data.split("_")[1]
        print(post_id)
        post = get_post(uid=post_id)
        print(post)
        print(type(post))
        pictures = post["pic"]
        print(type(pictures))
        media = [types.InputMediaPhoto(media=pic_url, caption=post['info'] if i == 0 else '', parse_mode='HTML') for i, pic_url in enumerate(pictures)]
        target = bot.send_media_group(chat_id=admin, media=media)
        bot.send_message(chat_id=call.message.chat.id,text="Sizning so'rovingiz adminga yuborildi. Javobini tez orada bilib olasiz")
        bot.send_message(chat_id=admin,text="...",reply_to_message_id=target[0].message_id,reply_markup=admin_yes_no(uid=post_id,cid=call.message.chat.id))
    elif "no-post" in call.data:
        bot.send_message(chat_id=call.message.chad.id,text="Bekor qilindi")
    elif "yes-admin" in call.data:
        post_id = call.data.split("_")[1]
        client_cid = call.data.split("_")[2]
        post = get_post(uid=post_id)
        pictures = post["pic"]
        media = [types.InputMediaPhoto(media=pic_url, caption=post['info'] if i == 0 else '', parse_mode='HTML') for i, pic_url in enumerate(pictures)]
        target = bot.send_media_group(chat_id=channel_id, media=media)
        bot.send_message(chat_id=call.message.chat.id,text="Kanalga yuborildi")
        bot.send_message(chat_id=client_cid,text="Postingiz kanalga joylandi!")
    elif "no-admin" in call.data:
        bot.send_message(chat_id=call.message.chat.id,text="Bekor qilindi")
        bot.send_message(chat_id=client_cid,text="So'rovingiz bekor qilindi")
        
@bot.message_handler(content_types=['photo', 'text'])
def main_funks(msg: types.Message):
    text = msg.text
    cid = msg.chat.id
    step = get_step(cid=cid)
    
    if step == "get_photos":
        if cid not in user_images:
            user_images[cid] = []

        if msg.photo or msg.text:
            try:
                try:
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
                except:
                    print("Bu rasm emas")
                # Check if 4 images are collected
                if len(user_images[cid]) == 4 or msg.text == "Tasdiqlash ✅":
                    if len(user_images[cid]) != 0:
                        img_x = json.dumps(user_images[cid])

                        change_info(cid=cid, type_info="pic", value=img_x)
                        bot.send_message(chat_id=msg.chat.id, text="<b>Rasmlarni yuklash yakunlandi!\nAvtomobile modelini yuboring!\nMasalan:</b> <i>(Spark 2-pozitsiya sotiladi)</i>", parse_mode="html",reply_markup=keyboard_rm())
                        put_step(cid=msg.chat.id, step="name")
                        user_images[cid] = []  # Reset the list after sending
                    else:
                        bot.send_message(chat_id=cid,text="Siz rasm yubormadingiz, bu esa mumkin emas avval rasm yuborib keyin Tasdiqlash ✅ tugmasini bosing!")

            except Exception as e:
                print(f"Error: {e}")    
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

📞Nomer: {nomer}</i>

{rek_text}
"""
        media = [types.InputMediaPhoto(media=pic_url, caption=text_info if i == 0 else '', parse_mode='HTML') for i, pic_url in enumerate(rasm)]
        target = bot.send_media_group(chat_id=cid, media=media)
        uid = uuid4()
        create_post(uid=uid,pic=x['pic'],info=text_info)
        bot.send_message(chat_id=cid,text="Ushbu anketa to'grimi?",reply_to_message_id=target[0].message_id,reply_markup=post_yes_no(uid=uid))
        
        
    elif step in steps:
        change_info(cid=cid, type_info=step, value=text)
        x_index = steps.index(step)
        bot.send_message(cid, step_msg[steps[x_index + 1]], parse_mode="html")
        put_step(cid=cid, step=steps[x_index + 1])

print(bot.get_me())
bot.polling()
