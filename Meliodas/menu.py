from Meliodas import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Meliodas.utils.lang import *


fbuttons = InlineKeyboardMarkup(
        [
        [
            InlineKeyboardButton(
                text="Support Group", url="https://t.me/+2zyDnYSSA844MzE1"
            ),
            InlineKeyboardButton(
                text="Command", callback_data="bot_commands"
            )
        ], 
        [
            InlineKeyboardButton("Back", callback_data='startcq')
        ]
        ]
)

keyboard =InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="🇱🇷 English", callback_data="languages_en"
            ),
            InlineKeyboardButton(
                text="🇮🇩 Indonesia", callback_data="languages_id"
            )
        ],
        [
            InlineKeyboardButton(
                text="🇮🇹 Italiano", callback_data="languages_it"                       
            ), 
        ], 
        [  
            InlineKeyboardButton("Back", callback_data='startcq')
        ]
    ]
)

@app.on_callback_query(filters.regex("_langs"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    user = CallbackQuery.message.from_user.mention
    await app.send_message(
        CallbackQuery.message.chat.id,
        text= "The list of available languages:",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()
    
@app.on_callback_query(filters.regex("_about"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=_["menu"],
        reply_markup=fbuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()

