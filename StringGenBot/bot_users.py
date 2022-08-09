# Starting User Mod Interface by RishBroPromax

from pyrogram.types import Message
from pyrogram import Client, filters
from StringGenBot.db import SESSION
from StringGenBot.db.users_sql import Users, num_users

async def bot_sys_stats():
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    stats = f"""
>>>  String Session Bot Bot Details

• 💽 Tᴏᴛᴇʟ Dɪsᴋ Sᴘᴀᴄᴇ: {total}
• 💿 Usᴇᴅ Sᴘᴀᴄᴇ: {used}({disk_usage}%)
• 📊 Fʀᴇᴇ Sᴘᴀᴄᴇ: {free}
• 🔋 Cᴘᴜ Usᴀɢᴇ: {cpu_usage}%
• 🖲 Rᴀᴍ Usᴀɢᴇ: {ram_usage}%
• ⚡️ Tᴏᴛᴀʟ Usᴇʀs : {total_users}

>>> Powerd by [Cyber Bot SL](t.me/Cyber_Botz_SL)
>>> Support by [ImRishmika](t.me/ImRishmika)

"""

    return stats
