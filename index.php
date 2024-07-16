<?php
$db_username ='username';
$db_passwd = "password";
$admin = "admin_id";//
$nchannel="@channel"; //CHannel
$schannel = "@ads_channel";//Ads Channel
$rek_text = "🚗| @Jiguli_Maskvich_Bozori Канали
👉 https://t.me/+VcbND60PZvI6WqvW";
$bot_username = '@username_bot';
define("API_KEY","BOT_TOKEN");

function bot($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}
/*Functions by @Turgunboyev_Diyorbek*/
function send($chat_id,$text,$parse = 'html',$reply_markup = null){
    if($reply_markup == null){
        return bot('sendMessage',[
            'chat_id'=>$chat_id,
            'text'=>$text,
            'parse_mode'=>$parse
        ]);
    }else{
        return bot('sendMessage',[
            'chat_id'=>$chat_id,
            'text'=>$text,
            'parse_mode'=>$parse,
            'reply_markup'=>$reply_markup
        ]);
    }
}
function forward($from,$to,$mid){
    bot('forwardMessage',[
        'chat_id'=> $to,
        'from_chat_id'=>$from,
        'message_id'=>$mid
    ]);
}
function edit($chat_id,$message_id,$text,$parse_mode='html',$reply_markup=null){
    if($reply_markup == null){
        return bot('editMessagetext',[
            'chat_id'=>$chat_id,
            'message_id'=>$message_id,
            'text'=>$text,
            'parse_mode'=>$parse_mode
        ]);
    }else{
        return bot('editMessagetext',[
            'chat_id'=>$chat_id,
            'message_id'=>$message_id,
            'text'=>$text,
            'parse_mode'=>$parse_mode,
            'reply_markup'=>$reply_markup
        ]);
    }
}
function del($cid,$mid){
    bot('deleteMessage',[
        'chat_id'=>$cid,
        'message_id'=>$mid
    ]);
}
function get($name){
    return file_get_contents($name);
}
function put($name,$value){
    $put = file_put_contents($name, $value);
    if($put == false){
        return put($name,$value);
    }else{
        return $put;
    }
}
function dirs($dir){
    if(is_dir($dir)){}else{
        return mkdir($dir);
    }
}
function check($cid,$channel){
  $get = bot('getChatMember',[
    'chat_id'=>"@".$channel,
    'user_id'=>$cid
  ])->result->status;
  $ar = ["administrator","creator","member"];
  return in_array($get,$ar);
}
function clear($cid){
    $gl = glob("elon/$cid/*");
    $gl2 = array_map("unlink", $gl);
    return $gl2;
}

$update = json_decode(file_get_contents("php://input"));
$message = $update->message;
$cid = $message->chat->id;
$type = $message->chat->type;
$mid = $message->message_id;
$name = $message->chat->first_name;
$user = $message->from->username; $user = (empty($user))?"Kiritilmagan":"@".$user;
$text = $message->text;

$photo = $message->photo; $photo = (empty($photo))?[]:$photo;
$phid = $photo[count($photo)-1]->file_id;

$call = $update->callback_query;
/*$call_id = $call->inline_message_id;*/
$call_id = $call->id;
$data = $call->data;
$meme12 = $call->from->id;
$meme14 = $call->message->message_id;
$call_name = $call->from->first_name;

include "admin/panel.php";
$cfg = [
    "sql"=>[
        "host"=>"localhost",
        "user"=>"$db_username",
        "pass"=>"$db_passwd",
        "db"=>"u1578855_moshina"
    ]
];
$mem = new panel($cfg,API_KEY,$update);
$mem->create();
$mem->add();

$chid = ($message)?$cid:$meme12;

function step($step){
    global $chid;
    return file_put_contents("elon/$chid/ad.step",$step);
}

//----------------------
dirs("elon");
dirs("elon/$chid");

$stik = "elon/$chid/ad.step";
$step = get($stik);
//----------------------
$main = json_encode([
    'resize_keyboard'=>true,
    'keyboard'=>[
        [['text'=>"🔊E'lon berish"]],
        [['text'=>"📚Qo'llanma"]]
    ]
]);
$back = json_encode([
    'resize_keyboard'=>true,
    'keyboard'=>[
        [['text'=>"🔙Orqaga"],['text'=>"Bekor qilish❌"]]
    ]
]);
$next = json_encode([
    'resize_keyboard'=>true,
    'keyboard'=>[
        [['text'=>"Bekor qilish❌"],['text'=>"Keyingisi➡️"]]
    ]
]);
$bosh = json_encode([
    'resize_keyboard'=>true,
    'keyboard'=>[
        [['text'=>"🏡Bosh menu"]]
    ]
]);
$yesno = json_encode([
    'resize_keyboard'=>true,
    'keyboard'=>[
        [['text'=>"Ha✅"],['text'=>"Yo'q❌"]]
    ]
]);
$tasdiqlash = json_encode([
    'inline_keyboard'=>[
        [['text'=>"Tasdiqlash",'callback_data'=>"allow".$cid],['text'=>"Rad etish",'callback_data'=>"deny".$cid]]
    ]
]);
$remove = json_encode([
    'remove_keyboard'=>true
]);

if($text == "/start"){
    send($cid,"👋 Assalomu alaykum! <a href='tg://user?id=$cid'>$name</a>
E'lon berish uchun quyidagi \"🔊E'lon berish\" tugmasidan foydalaning!
\"📚Qo'llanma\" orqali qanday qilib e'lon berishni video orqalik ko'rib olishingiz mumkin!",'html',$main);
}
if($text == "📚Qo'llanma"){
	bot('sendVideo',[
		'chat_id'=>$cid,
		'video'=>"https://t.me/G0LDPHP/158",
		'caption'=>"<b>🤖 $bot_username da e'lon joylash qo'llanmasi.

✔️ Qulay va ishonchli e'lon berish!</b>

<i>E'lon yuborgandan keyin adminga yozib qo'yish esdan chiqmasin! 👨‍💻

😉 27,7 mb achinmaysiz ko'rsangiz</i>",
		'parse_mode'=>'html',
		'reply_markup'=>$main
	]);
}

if($text == "🔊E'lon berish"){
    send($cid,"<b>Avtomobilning 1-6 tagacha rasmini yuboring!\nRasmlarni yuborib bo'lgandan keyin quyidagi Keyingisi➡️ tugmasini bosing.\nEslatma:</b> <i>Har qanday rasm bo'lmagan kontent uchun e'lon berish to'xtatiladi!</i>",'html',$next);
    step("1");
}
if($text == "Bekor qilish❌" or $text == "Yo'q❌"){
    clear($cid);
    del($cid,$mid-1);
    send($cid,"E'lon berish to'xtatildi!\nAssalomu alaykum!\nE'lon berish uchun quyidagi 🔊E'lon berish tugmasidan foydalaning",'html',$main);
    exit();
}
if($step == "1"){
    if($photo){
        $ph1 = get("elon/$cid/photo.json");
        $ph2 = json_decode($ph1);
        $n = count($ph2);
        $path = bot('getFile',[
            'file_id'=>$phid
        ])->result->file_path;
        $file = "https://api.telegram.org/file/bot".API_KEY."/$path";
        if($n < 9){
            $phc = bot('sendPhoto',[
                'chat_id'=>$nchannel,
                'photo'=>"https://onlinebotlar.uz/Mashina/Moshina/api.php?url=$file"
            ]);
            $phid = $phc->result->message_id;
            $ph2[] = "$phid";
            put("elon/$cid/photo.json",json_encode($ph2));
        }elseif($n == 9){
            $phc = bot('sendPhoto',[
                'chat_id'=>$nchannel,
                'photo'=>"https://onlinebotlar.uz/Mashina/Moshina/api.php?url=$file"
            ]);
            $phid = $phc->result->message_id;
            $ph2[] = "$phid";
            put("elon/$cid/photo.json",json_encode($ph2));
            send($cid,"<b>Rasmlarni yuklash yakunlandi!
Avtomobil modelini yuboring!
Masalan:</b> <i>(Spark 2-pozitsiya sotiladi)</i>",'html',$back);
            step("2");
        }
    }
    if($text == "Keyingisi➡️"){
        $ph1 = get("elon/$cid/photo.json");
        $ph2 = json_decode($ph1);
        $n = count($ph2);
        if($n >= 1){
            send($cid,"<b>Rasmlarni yuklash yakunlandi!
Avtomobile modelini yuboring!
Masalan:</b> <i>(Spark 2-pozitsiya sotiladi)</i>",'html',$back);
            step("2");
        }else{
            send($cid,"<b>Siz hali birorta ham rasm yuklamadingiz!\nIltimos avval rasm yuklang va keyin ushbu tugmadan foydalaning</b>");
        }
        exit();
    }
    if(!isset($photo) and $message){
        unlink("elon/$cid/photo.json");
        unlink($stik);
        del($cid,$mid-1);
        send($cid,"E'lon berish to'xtatildi!\nAssalomu alaykum!\nE'lon berish uchun quyidagi 🔊E'lon berish tugmasidan foydalaning",'html',$main);
    }
}
if($step == "2"){
    if($text == "🔙Orqaga"){
        send($cid,"<b>Avtomobilning 1-6 tagacha rasmini yuboring!\nRasmlarni yuborib bo'lgandan keyin quyidagi Keyingisi➡️ tugmasini bosing\nEslatma:</b> <i>Har qanday rasm bo'lmagan kontent uchun e'lon berish to'xtatiladi!</i>",'html',$next);
        step("1");
        unlink("elon/$cid/photo.json");
        exit();
    }
    
    if($text){
        put("elon/$cid/model.txt",$text);
        send($cid,"<b>Ishlab chiqarilgan yilni yozing.\nMasalan:</b> <i>(2010 yil)</i>",'html',$back);
        step("2.5");
    }
}

ifif($step == "2.5"){
    if($text == "🔙Orqaga"){
        send($cid,"<b>Avtomobilning 1-6 tagacha rasmini yuboring!\nRasmlarni yuborib bo'lgandan keyin quyidagi Keyingisi➡️ tugmasini bosing\nEslatma:</b> <i>Har qanday rasm bo'lmagan kontent uchun e'lon berish to'xtatiladi!</i>",'html',$next);
        step("1");
        unlink("elon/$cid/photo.json");
        exit();
    }
    
    if($text){
        put("elon/$cid/km.txt",$text);
        send($cid,"<b>Yurgan yo'lni yozingni yozing.\nMasalan:</b> <i>(100.000km)</i>",'html',$back);
        step("3");
    }    
}


if($step == "3"){
    if($text == "🔙Orqaga"){
        send($cid,"<b>Yurgan yo'lni yozingni yozing.\nMasalan:</b> <i>(100.000km)</i>",'html',$back);
        step("2.5");
        unlink("elon/$cid/km.txt");
        exit();
    }
    
    if($text){
        put("elon/$cid/date.txt",$text);
        send($cid,"<b>Yoqilgi turini yozing!\nMasalan:</b> <i>(Benzin + metan)</i>",'html',$back);
        step("4");
    }
}
if($step == "4"){
    if($text == "🔙Orqaga"){
        send($cid,"<b>Ishlab chiqarilgan yil va yurgan kilometrni yozing.\nMasalan:</b> <i>(2010 yil, 100,000 km).</i>",'html',$back);
        step("3");
        unlink("elon/$cid/date.txt");
        exit();
    }
    
    if($text){
        put("elon/$cid/gas.txt",$text);
        send($cid,"<b>Texnik holatini yozing!\nMasalan:</b> <i>(Toza urilmagan).</i>",'html',$back);
        step("5");
    }
}
if($step == "5"){
    if($text == "🔙Orqaga"){
        send($cid,"<b>Yoqilgi turini yozing!\nMasalan:</b> <i>(Benzin + metan)</i>",'html',$back);
        step("4");
        unlink("elon/$cid/gas.txt");
        exit();
    }
    
    if($text){
        put("elon/$cid/texnika.txt",$text);
        send($cid,"<b>🎨 Kraskasi haqida yozing!\nMasalan:</b> <i>(Ozgina petno bor 15 foiz)</i>",'html',$back);
        step("11");
    }
}

if($step == "11"){
    if($text == "🔙Orqaga"){
        send($cid,"<b>Texnik holatini yozing!\nMasalan:</b> <i>(Toza urilmagan).</i>",'html',$back);
        step("5");
        unlink("elon/$cid/texnika.txt");
        exit();
    }

    if($text){
        put("elon/$cid/kraska.txt",$text);
        send($cid,"<b>Qo'shimcha ma'lumot yozing!\nMasalan:</b> <i>(Navarotlari, tonirovka ruxsatnomasi, majigar, kalonkalari haqida)</i>",'html',$back);
        step("6");
    }
}

if($step == "6"){
    if($text == "🔙Orqaga"){
        send($cid,"<b>🎨 Kraskasi haqida yozing!\nMasalan:</b> <i>(Ozgina petno bor 15 foiz)</i>",'html',$back);
        step("11");
        unlink("elon/$cid/kraska.txt");
        exit();
    }
    
    if($text){
        put("elon/$cid/qoshimcha.txt",$text);
        send($cid,"<b>Narxini yozing!\nMasalan:</b> <i>(10,000$ yoki 10 million so'm)</i>",'html',$back);
        step("7");
    }
}
if($step == "7"){
    if($text == "🔙Orqaga"){
        send($cid,"<b>Qo'shimcha malumot yozing!\nMasalan:</b> <i>(Navarotlari bor, hujjatlari bor, tonirovka ruxsat bor, majigar, kolonka)</i>",'html',$back);
        step("6");
        unlink("elon/$cid/qoshimcha.txt");
        exit();
    }
    
    if($text){
        put("elon/$cid/narx.txt",$text);
        send($cid,"<b>Manzilni kiriting(Viloyat,shahar,tuman)!\nMasalan:</b> <i>(Toshkent, Chirchiq)</i>",'html',$back);
        step("8");
    }
}
if($step == "8"){
    if($text == "🔙Orqaga"){
        send($cid,"<b>Narxini yozing!\nMasalan:</b> <i>(10,000$ yoki 10 million so'm)</i>",'html',$back);
        step("7");
        unlink("elon/$cid/narx.txt");
        exit();
    }
    
    if($text){
        put("elon/$cid/manzil.txt",$text);
        send($cid,"<b>Telefon raqamlaringizni kiriting.\nMasalan:</b> <i>(+998901234567)</i>",'html',$back);
        step("9");
    }
}
if($step == "9"){
    if($text == "🔙Orqaga"){
        send($cid,"<b>Manzilni kiriting(Viloyat,shahar,tuman)!\nMasalan:</b> <i>(Toshkent, Chirchiq)</i>",'html',$back);
        step("8");
        unlink("elon/$cid/manzil.txt");
        exit();
    }
    
    if(mb_stripos($text, "+998")!==false){
        put("elon/$cid/nomer.txt",$text);
        step("10");
        $rasm = json_decode(get("elon/$cid/photo.json"));
        $model = get("elon/$cid/model.txt");
        $sana = get("elon/$cid/date.txt");
        $km = get("elon/$cid/km.txt");
        $gas = get("elon/$cid/gas.txt");
        $texnik = get("elon/$cid/texnika.txt");
        $qoshimcha = get("elon/$cid/qoshimcha.txt");
        $narx = get("elon/$cid/narx.txt");
        $manzil = get("elon/$cid/manzil.txt");
        $kraska = get("elon/$cid/kraska.txt");
        $nomer = $text;

        if(count($rasm) > 1){
            $photos = [];
            foreach($rasm as $ids){
                $photos[] = ['type'=>'photo','media'=>"https://t.me/".(explode("@", $nchannel))[1]."/".$ids];
            }
            $photos[count($photos)-1]['caption'] = "<b>🚗| $model</b>

<i>📆Yili: $sana
🚦Km: $km
⛽️Yoqilg'i: $gas
🛠Texnik holati: $texnik
🎨Kraska: $kraska
🔰Qo'shimcha: $qoshimcha</i>
<b>💰Narxi: $narx

📍Manzil: $manzil</b>

📞Nomer: $nomer

$rek_text";
            $photos[count($photos)-1]['parse_mode'] = 'html';
            bot('sendMediaGroup',[
                'chat_id'=>$cid,
                'media'=>json_encode($photos)
            ]);
            send($cid,"Yuqorida berilgan ma'lumotlar to'g'rimi?(Eslatib o'tamiz Yo'q tugmasi bosilganda e'lon berish qaytadan boshlanadi)",'html',$yesno);
        }else{
            bot('sendPhoto',[
                'chat_id'=>$cid,
                'photo'=>"https://t.me/".(explode("@", $nchannel))[1]."/".$rasm[0],
                'caption'=>"<b>🚗| $model</b>

<i>📆Yili: $sana
🚦Km: $km
⛽️Yoqilg'i: $gas
🛠Texnik holati: $texnik
🎨Kraska: $kraska
🔰Qo'shimcha: $qoshimcha</i>
<b>💰Narxi: $narx

📍Manzil: $manzil</b>

📞Nomer: $nomer

$rek_text",
                'parse_mode'=>'html'
            ]);
            send($cid,"Yuqorida berilgan ma'lumotlar to'g'rimi?(Eslatib o'tamiz Yo'q tugmasi bosilganda e'lon berish qaytadan boshlanadi)",'html',$yesno);
        }
    }else{
        send($cid,"<b>Iltimos telefon raqamingizni namunadagidek yuboring.\nNamuna:</b> <i>(<u>+998</u>901234567)</i>",'html',$back);
    }
}

if($text == "Ha✅" and $step == "10"){
    $rasm = json_decode(get("elon/$cid/photo.json"));
    $model = get("elon/$cid/model.txt");
    $sana = get("elon/$cid/date.txt");
    $gas = get("elon/$cid/gas.txt");
    $texnik = get("elon/$cid/texnika.txt");
    $qoshimcha = get("elon/$cid/qoshimcha.txt");
    $narx = get("elon/$cid/narx.txt");
    $manzil = get("elon/$cid/manzil.txt");
    $kraska = get("elon/$cid/kraska.txt");
    $nomer = get("elon/$cid/nomer.txt");

    if(count($rasm) > 1){
        $photos = [];
        foreach($rasm as $ids){
            $photos[] = ['type'=>'photo','media'=>"https://t.me/".(explode("@", $nchannel))[1]."/".$ids];
        }
        $photos[count($photos)-1]['caption'] = "<b>🚗| $model</b>

<i>📆Yili: $sana
🚦Km: $km
⛽️Yoqilg'i: $gas
🛠Texnik holati: $texnik
🎨Kraska: $kraska
🔰Qo'shimcha: $qoshimcha</i>
<b>💰Narxi: $narx

📍Manzil: $manzil</b>

📞Nomer: $nomer

$rek_text";
        $photos[count($photos)-1]['parse_mode'] = 'html';
        send($cid,"<b>E'lonni tasdiqlash uchun adminga yuborildi! Agarda sizning e'loningizda kamchiliklar bolmasa, biz tez orada sizning e'loningizni kanalimizga joylaymiz!</b>\n\nYuborilgan e'lon kanalimizga joylanishi uchun @Jiguli_Admin ga e'lon yuborganligingiz haqida xabar berishingiz so'raladi!
Hurmat bilan @Jiguli_Maskvich_Bozori",'html',$main);
            //-----------------------------------------------------------------
        bot('sendMediaGroup',[
            'chat_id'=>$admin,
            'media'=>json_encode($photos)
        ]);
        send($admin,"Yangi e'lon!\nID: $cid\nIsm: <a href='tg://user?id=$cid'>$name</a>\nUsername: $user",'html',$tasdiqlash);
    }else{
        send($cid,"<b>E'lonni tasdiqlash uchun adminga yuborildi! Agarda sizning e'loningizda kamchiliklar bolmasa, biz tez orada sizning e'loningizni kanalimizga joylaymiz!</b>\n\nYuborilgan e'lon kanalimizga joylanishi uchun @Jiguli_Admin ga e'lon yuborganligingiz haqida xabar berishingiz so'raladi!
Hurmat bilan @Jiguli_Maskvich_Bozori",'html',$main);
        //---------------------------------------------------------------------
        bot('sendPhoto',[
            'chat_id'=>$admin,
            'photo'=>"https://t.me/".(explode("@", $nchannel))[1]."/".$rasm[0],
            'caption'=>"<b>🚗| $model</b>

<i>📆Yili: $sana
🚦Km: $km
⛽️Yoqilg'i: $gas
🛠Texnik holati: $texnik
🎨Kraska: $kraska
🔰Qo'shimcha: $qoshimcha</i>
<b>💰Narxi: $narx

📍Manzil: $manzil</b>

📞Nomer: $nomer

$rek_text",
                'parse_mode'=>'html'
        ]);
        send($admin,"Yangi e'lon!\nID: $cid\nIsm: <a href='tg://user?id=$cid'>$name</a>\nUsername: $user",'html',$tasdiqlash);
    }
}

if(mb_stripos($data, "allow")!==false){
    bot('answerCallbackQuery',[
        'callback_query_id'=>$call_id,
        'text'=>"E'lon kanalga muvaffaqiyatli joylandi!",
        'show_alert'=>true
    ]);
    $ex = explode("allow", $data);
    /*del($meme12,$meme14);*/
    send($ex[1],"<b>Sizning e'loningiz kanalimizga joylandi!\nBizning xizmatdan foydalanganingizdan mamnunmiz😊</b>",'html',$main);

    $cid = $ex[1];

    $rasm = json_decode(get("elon/$cid/photo.json"));
    $rasm = (is_object($rasm))?get_object_vars($rasm):$rasm;
    $model = get("elon/$cid/model.txt");
    $sana = get("elon/$cid/date.txt");
    $gas = get("elon/$cid/gas.txt");
    $texnik = get("elon/$cid/texnika.txt");
    $qoshimcha = get("elon/$cid/qoshimcha.txt");
    $narx = get("elon/$cid/narx.txt");
    $manzil = get("elon/$cid/manzil.txt");
    $nomer = get("elon/$cid/nomer.txt");
    $kraska = get("elon/$cid/kraska.txt");

    if(count($rasm) > 1){
        $photos = [];
        foreach($rasm as $ids){
            $photos[] = ['type'=>'photo','media'=>"https://t.me/".(explode("@", $nchannel))[1]."/".$ids];
        }
        $photos[count($photos)-1]['caption'] = "<b>🚗| $model</b>

<i>📆Yili: $sana
🚦Km: $km
⛽️Yoqilg'i: $gas
🛠Texnik holati: $texnik
🎨Kraska: $kraska
🔰Qo'shimcha: $qoshimcha</i>
<b>💰Narxi: $narx

📍Manzil: $manzil</b>

📞Nomer: $nomer

$rek_text";
        $photos[count($photos)-1]['parse_mode'] = 'html';
        //-----------------------------------------------------------------
        bot('sendMediaGroup',[
            'chat_id'=>$schannel,
            'media'=>json_encode($photos)
        ]);
        clear($cid);
    }else{
        //---------------------------------------------------------------------
        bot('sendPhoto',[
            'chat_id'=>$schannel,
            'photo'=>"https://t.me/".(explode("@", $nchannel))[1]."/".$rasm[0],
            'caption'=>"<b>🚗| $model</b>

<i>📆Yili: $sana
🚦Km: $km
⛽️Yoqilg'i: $gas
🛠Texnik holati: $texnik
🎨Kraska: $kraska
🔰Qo'shimcha: $qoshimcha</i>
<b>💰Narxi: $narx

📍Manzil: $manzil</b>

📞Nomer: $nomer

$rek_text",
                'parse_mode'=>'html'
        ]);
        clear($cid);
    }
}
if(mb_stripos($data, "deny")!==false){
    /*del($meme12,$meme14);
    del($meme12,$meme14-1);*/
    bot('answerCallbackQuery',[
        'callback_query_id'=>$call_id,
        'text'=>"E'lon rad etildi!",
        'show_alert'=>true
    ]);
    $ex = explode("deny", $data);
    send($ex[1],"<b>Sizning e'loningiz rad etildi!\nUni ko'rib chiqib qayta e'lon berishingiz mumkin!</b>",'html',$main);
    clear($ex[1]);
}