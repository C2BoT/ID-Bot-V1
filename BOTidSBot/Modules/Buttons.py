from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

ID_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("π‘ππͺ π¬π’π₯π β", url="t.me/us7a5")
       ]]
       )
INFO_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("π‘ππͺ π¬π’π₯π β", url="t.me/us7a5")
       ]]
       )
ID_BUTTONS = InlineKeyboardMarkup( [[
       InlineKeyboardButton("βοΈ πΆπ΄π πΈπ½π΅πΎππΌπ°ππΈπΎπ½ βοΈ", callback_data="info")
       ],[
       InlineKeyboardButton("π π±π°π²πΊ ππΎ π·π΄π»πΏ π", callback_data="help")
       ]]
       )
INFO_BUTTONS = InlineKeyboardMarkup( [[
       InlineKeyboardButton("βοΈ ππ΄π»π΄πΆππ°πΌ πΈπ³ βοΈ", callback_data="id")
       ],[
       InlineKeyboardButton("π π±π°π²πΊ ππΎ π·π΄π»πΏ π", callback_data="help")
       ]]
       )
JSON_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("π‘ππͺ π¬π’π₯π β", url="t.me/us7a5")
       ]]
       )
