import os
import re
from platform import python_version as kontol
from telethon import events, Button
from Messi.events import register
from Messi import telethn as tbot


PHOTO = "https://telegra.ph/file/9b2f5c511b0ecdfbabdcf.mp4"

@register(pattern=("bancodes"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Lionell Messi** \n\n"
  TEXT += "🗡 **Here are bancodes for [Messi](https://t.me/messi_probot)** \n\n"
  TEXT += f"🗡 **My Masters : [Messi Probot Team](https://t.me/Messi_Probot_Team)** \n\n"
  TEXT += f"🗡 **Library Version :** `{x}` \n\n"
  TEXT += f"🗡 **Telethon Version :** `{y}` \n\n"
  TEXT += f"🗡 **Pyrogram Version :** `{z}` \n\n"
  TEXT += "**⚽️ Thanks For Starting Me ⚽️**"
  BUTTON = [[Button.url("Help", "https://t.me/Messi_Probot?start=help"), Button.url("My Headquarters", "https://t.me/Messi_Probot_SUpport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
