import asyncio
import time
from inspect import getfullargspec
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client
from pyrogram.types import Message
from Python_ARQ import ARQ
import asyncio
from pyrogram import Client
from config import *
import pymongo


SUPPORT_GROUP = "https://t.me/OfficiallMeliodas"
SUDOERS = SUDO_USERS_ID
LOG_GROUP_ID = LOG_GROUP_ID
MOD_LOAD = []
MOD_NOLOAD = []
bot_start_time = time.time()
DB_URI = BASE_DB 
MONGO_URL = MONGO_URL
OWNER_ID = 5097913434


myclient = pymongo.MongoClient(DB_URI)
dbn = myclient["denz"]

mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client.wbb


loop = asyncio.get_event_loop()
aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

bot = Client("denz", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
bot.start()
app = Client("app2", bot_token=BOT_TOKEN, api_id=API_ID1, api_hash=API_HASH1)
app.start()

x = app.get_me()

BOT_ID = int(BOT_TOKEN.split(":")[0])
BOT_NAME = x.first_name + (x.last_name or "")
BOT_USERNAME = x.username
BOT_MENTION = x.mention
BOT_DC_ID = x.dc_id

async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})
