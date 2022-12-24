'''import os
import re
import random

from platform import python_version as kontol
from telethon import events, Button
from Messi.events import register
from Messi import telethn as tbot


PHOTO = "https://telegra.ph/file/f8f96fc3fed17875a0673.jpg"

@register(pattern=("Awake"))
async def awake(event):
  TEXT = f"""Hi {event.sender.first_name}, I'm Lionell Messi ."""\n
  TEXT += f"❄Messi Is Alive ⚽️**"\n\n
  TEXT += f"❄My Domain : [FIFA](https://t.me/Fifa_Federation)**"\n\n
  TEXT += f"❄ **Powered By: [Messi Team](https://t.me/Messi_Probot_Team)**"\n\n
   Thanks For Adding Me Here ❤️ re ❤️ **"
  BUTTON = [[Button.url("Help", "https://t.me/messi_probot?start=help"), Button.url("My Home", "https://t.me/Messi_Probot_Support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
'''
