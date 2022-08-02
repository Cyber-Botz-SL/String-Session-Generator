from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🎊 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🎊 ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("⚙ sᴜᴩᴩᴏʀᴛ", url="https://t.me/Cyber_Botz_SL"),
         InlineKeyboardButton("👨‍💻 ᴅᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/Dr_Stranger_XD"),
        ],
    ]

    START = """
Hᴇʏ {},

Tʜɪs ɪs {},
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Sᴏᴜʀᴄᴇ : [ɢɪᴛʜᴜʙ](https://github.com/Cyber-Botz-SL)
Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [𝘿𝙍 𝙎𝙏𝙍𝘼𝙉𝙂𝙀𝙍🇱🇰](https://t.me/Dr_Stranger_XD) !
    """
