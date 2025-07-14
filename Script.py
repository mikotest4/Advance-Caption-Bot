import os

class script(object):

    START_TXT = """<b>Hᴇʟʟᴏ {}\n\n
ɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ ᴀɴᴅ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴ ꜰᴇᴀᴛᴜʀᴇ, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ cʜᴀɴɴᴇʟ ᴀɴᴅ ᴇɴᴊᴏʏ

‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/Silicon_Bot_Update'>Sɪʟɪᴄᴏɴ Bᴏᴛ</a></b>
"""

    HELP_TXT = """•••[( 𝘎𝘦𝘵 𝘏𝘦𝘭𝘱 )]•••

❗ 𝗔𝗹𝗲𝗿𝘁 ❗

• Aᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
• Usᴇ ᴄᴏᴍᴍᴀɴᴅ ɢɪᴠᴇ ʙᴇʟᴏᴡ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟ.
• Kᴇᴇᴘ ғɪʟᴇ ᴡɪᴛʜᴏᴜᴛ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ.

<b>📋 Cʜᴀɴɴᴇʟ Cᴏᴍᴍᴀɴᴅs:</b>
•> /set_cap - Sᴇᴛ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Iɴ ʏᴏᴜʀ Cʜᴀɴɴᴇʟ
•> /del_cap - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ

<b>🎯 Rᴀɴᴅᴏᴍ Cᴀᴘᴛɪᴏɴ Cᴏᴍᴍᴀɴᴅs (Aɴʏ Usᴇʀ):</b>
•> /add_caption <caption> - Aᴅᴅ ɴᴇᴡ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴ
•> /list_captions - Lɪsᴛ ᴀʟʟ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴs
•> /total_captions - Tᴏᴛᴀʟ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴs ᴄᴏᴜɴᴛ
•> /del_caption <caption_id> - Dᴇʟᴇᴛᴇ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴ

<b>📱 Sᴜᴘᴘᴏʀᴛᴇᴅ Mᴇᴅɪᴀ:</b>
✅ Photos
✅ Videos  
✅ Audio Files
✅ Documents
✅ Voice Messages
✅ Video Notes
✅ GIFs/Animations
✅ Stickers

𝑭𝒐𝒓𝒎𝒂𝒕 𝑽𝒂𝒓𝒊𝒂𝒃𝒍𝒆𝒔:
`{file_name}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Nᴀᴍᴇ
`{file_size}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Sɪᴢᴇ 
`{language}` = Lᴀɴɢᴜᴀɢᴇ Oғ Fɪʟᴇ Nᴀᴍᴇ
`{year}` = Yᴇᴀʀ Oғ Fɪʟᴇ
`{media_type}` = Tʏᴘᴇ ᴏғ Mᴇᴅɪᴀ
`{default_caption}` = Rᴇᴀʟ Cᴀᴘᴛɪᴏɴ Oғ Fɪʟᴇ

Eg:- `/set_cap
{file_name}

⚙️ Size » {file_size}
📁 Type » {media_type}

╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
💥 𝙅𝙊𝙄𝙉 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ 
💥 𝙅𝙊𝙄𝙉 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ
╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝`
"""

    ABOUT_TXT = """<b>╔════❰ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : <a href='https://t.me/CustomCaptionBot'>Auto Caption</a>
║┣⪼👦Cʀᴇᴀᴛᴏʀ : <a href='https://t.me/Silicon_Official'>Sɪʟɪᴄᴏɴ Dᴇᴠᴇʟᴏᴘᴇʀ ⚠️</a>
║┣⪼🤖Uᴘᴅᴀᴛᴇ : <a href='https://t.me/Silicon_Bot_Update'>Sɪʟɪᴄᴏɴ Bᴏᴛᴢ™</a>
║┣⪼📡Hᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ 
║┣⪼🗣️Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ3
║┣⪼📚Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ 2.11.6
║┣⪼🗒️Vᴇʀsɪᴏɴ : 3.1.0 [ᴀʟʟ ᴍᴇᴅɪᴀ sᴜᴘᴘᴏʀᴛ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁

🎯 <b>Nᴇᴡ Fᴇᴀᴛᴜʀᴇs:</b>
• Rᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴ sᴇʟᴇᴄᴛɪᴏɴ
• Aʟʟ ᴍᴇᴅɪᴀ ᴛʏᴘᴇs sᴜᴘᴘᴏʀᴛ
• Aɴʏ ᴜsᴇʀ ᴄᴀɴ ᴀᴅᴅ ᴄᴀᴘᴛɪᴏɴs
• 100+ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴs sᴜᴘᴘᴏʀᴛ
• Gʀᴏᴜᴘ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ sᴜᴘᴘᴏʀᴛ</b>"""
