import asyncio
import sys
import logging as log

from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from Messi.config import *
from Messi.confing import get_int_key, get_str_key

MONGO_DB = "Messi"

client = MongoClient()
client = MongoClient("mongodb+srv://archisman:Rick_2005@cluster0.ts8ihph.mongodb.net/?retryWrites=true&w=majority", 27017)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient("mongodb+srv://archisman:Rick_2005@cluster0.ts8ihph.mongodb.net/?retryWrites=true&w=majority", 27017)
db = motor[MONGO_DB]
db = client["emiexrobot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
