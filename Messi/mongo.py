import asyncio
import sys
import logging as log

from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from Messi import MONGO_DB_URI
from Messi.confing import get_int_key, get_str_key


MONGO_PORT = get_int_key("27017")
MONGO_DB_URI = get_str_key("MONGO_DB_URI")
MONGO_DB = "EmikoRobot"


client = MongoClient()
client = MongoClient("mongodb+srv://archisman:Rick_2005@cluster0.ts8ihph.mongodb.net/?retryWrites=true&w=majority", 27017)[Messi]
motor = motor_asyncio.AsyncIOMotorClient("mongodb+srv://archisman:Rick_2005@cluster0.ts8ihph.mongodb.net/?retryWrites=true&w=majority", 27017)
db = motor[Messi]
db = client["emiexrobot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
