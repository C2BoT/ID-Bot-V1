from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("π π±π",  url=f"tg://openmessage?user_id=1257421053"),
       InlineKeyboardButton("πΊπ² π±π", url=f"tg://openmessage?user_id=2146813672")
       ],[
       InlineKeyboardButton("β¬οΈ πΌπΎππ΄ πΈπ½π΅πΎππΌπ°ππΈπΎπ½ β¬οΈ", callback_data="help")
       ],[
       InlineKeyboardButton("β π½π΄π ππΎππΊ β", url=f"https://t.me/us7a5")
       ],[
       InlineKeyboardButton("β π²π»πΎππ΄", callback_data="close")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("ππ΄π»π΄πΆππ°πΌ πΈπ³", callback_data="id"),
       InlineKeyboardButton("ππ΄π»π΄πΆππ°πΌ πΈπ½π΅πΎ", callback_data="info")
       ],[
       InlineKeyboardButton("π  π·πΎπΌπ΄", callback_data="start"),
       InlineKeyboardButton("β π²π»πΎππ΄", callback_data="close"),
       InlineKeyboardButton("πΈ π°π±πΎππ", callback_data="about")
       ]]
       )

ABOUT_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("π π±π°π²πΊ", callback_data="help"),
       InlineKeyboardButton("π  π·πΎπΌπ΄", callback_data="start"),
       InlineKeyboardButton("β π²π»πΎππ΄", callback_data="close")
       ]]
       )
