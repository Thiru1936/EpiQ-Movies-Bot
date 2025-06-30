import os

class Config(object):

  FSUB_CHANNEL = os.environ.get("FSUB_CHANNEL", [])
  if FSUB_CHANNEL:
    FSUB_CHANNEL = [int(x) for x in FSUB_CHANNEL.split()]
    
  API_ID = int(os.environ.get("API_ID", "23060811"))
  API_HASH = os.environ.get("API_HASH", "6845600d24b8760ab0c23a352e893222")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "dashboard.gyanilinks.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "74144fdbaa5e91fc2f1f85868df0d43f1fa1daa2")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5829893945"))
  BOT_ADMINS = set(int(x) for x in os.environ.get("BOT_ADMINS", "5829893945").split())
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002847593493")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002813267918"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f""" hi
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\n **Hᴇʟʟᴏ Stranger🦋 ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ Fɪʟᴇ ᴛᴏ ʟɪɴᴋ + ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ **⚡️
"""
