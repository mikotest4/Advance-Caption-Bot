import os

class script(object):

    START_TXT = """<b>Hᴇʟʟᴏ {}\n\n
ɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ ᴀɴᴅ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴ ꜰᴇᴀᴛᴜʀᴇ, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ cʜᴀɴɴᴇʟ ᴀɴᴅ ᴇɴᴊᴏʏ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴs!

‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/Silicon_Bot_Update'>Sɪʟɪᴄᴏɴ Bᴏᴛ</a></b>
"""

    HELP_TXT = """•••[( 𝘎𝘦𝘵 𝘏𝘦𝘭𝘱 )]•••

❗ 𝗔𝗹𝗲𝗿𝘁 ❗

• Aᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
• Bᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴅᴅs ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴs ON TOP ᴏғ ᴏʀɪɢɪɴᴀʟ ᴄᴀᴘᴛɪᴏɴs.
• Aɴʏᴏɴᴇ ᴄᴀɴ ᴛᴜʀɴ ON/OFF ᴛʜᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ғᴇᴀᴛᴜʀᴇ.

<b>⚡ Bot Control Commands (Anyone Can Use):</b>
•> /bot_on - Tᴜʀɴ ON ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴄᴀᴘᴛɪᴏɴ ғᴇᴀᴛᴜʀᴇ
•> /bot_off - Tᴜʀɴ OFF ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴄᴀᴘᴛɪᴏɴ ғᴇᴀᴛᴜʀᴇ
•> /bot_status - Cʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ʙᴏᴛ sᴛᴀᴛᴜs

<b>🔧 Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅs (Rᴀɴᴅᴏᴍ Cᴀᴘᴛɪᴏɴ Mᴀɴᴀɢᴇᴍᴇɴᴛ):</b>
•> /add_caption <caption> - Aᴅᴅ ɴᴇᴡ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴ (Admin Only)
•> /list_captions - Lɪsᴛ ᴀʟʟ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴs (Admin Only)
•> /total_captions - Tᴏᴛᴀʟ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴs ᴄᴏᴜɴᴛ (Admin Only)
•> /del_caption <caption_id> - Dᴇʟᴇᴛᴇ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴ (Admin Only)
•> /clear_captions - Cʟᴇᴀʀ ᴀʟʟ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴs (Admin Only)

<b>👥 Pᴜʙʟɪᴄ Cᴏᴍᴍᴀɴᴅs (Aɴʏᴏɴᴇ Cᴀɴ Usᴇ):</b>
•> /bot_on - Tᴜʀɴ ᴏɴ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴄᴀᴘᴛɪᴏɴs
•> /bot_off - Tᴜʀɴ ᴏғғ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴄᴀᴘᴛɪᴏɴs
•> /bot_status - Cʜᴇᴄᴋ ʙᴏᴛ sᴛᴀᴛᴜs
•> /total_captions - Sᴇᴇ ᴛᴏᴛᴀʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴀᴘᴛɪᴏɴs
•> /preview_captions - Pʀᴇᴠɪᴇᴡ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴs

<b>📱 Sᴜᴘᴘᴏʀᴛᴇᴅ Mᴇᴅɪᴀ:</b>
✅ Photos
✅ Videos  
✅ Audio Files
✅ Documents
✅ Voice Messages
✅ Video Notes
✅ GIFs/Animations
✅ Stickers

<b>🎯 Hᴏᴡ Iᴛ Wᴏʀᴋs:</b>
1. Aᴅᴍɪɴ ᴀᴅᴅs 100+ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴs
2. Aɴʏᴏɴᴇ ᴄᴀɴ ᴛᴜʀɴ ʙᴏᴛ ON ᴜsɪɴɢ /bot_on
3. Usᴇʀs ᴘᴏsᴛ ᴀɴʏ ᴍᴇᴅɪᴀ
4. Bᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴅᴅs:
   📍 Rᴀɴᴅᴏᴍ Cᴀᴘᴛɪᴏɴ (TOP)
   📍 Oʀɪɢɪɴᴀʟ Cᴀᴘᴛɪᴏɴ (BOTTOM)
5. Aɴʏᴏɴᴇ ᴄᴀɴ ᴛᴜʀɴ OFF ᴜsɪɴɢ /bot_off
"""

    ABOUT_TXT = """<b>╔════❰ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : <a href='https://t.me/CustomCaptionBot'>Auto Caption</a>
║┣⪼👦Cʀᴇᴀᴛᴏʀ : <a href='https://t.me/Silicon_Official'>Sɪʟɪᴄᴏɴ Dᴇᴠᴇʟᴏᴘᴇʀ ⚠️</a>
║┣⪼🤖Uᴘᴅᴀᴛᴇ : <a href='https://t.me/Silicon_Bot_Update'>Sɪʟɪᴄᴏɴ Bᴏᴛᴢ™</a>
║┣⪼📡Hᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ 
║┣⪼🗣️Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ3
║┣⪼📚Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ 2.11.6
║┣⪼🗒️Vᴇʀsɪᴏɴ : 7.0.0 [ᴘᴜʙʟɪᴄ ON/OFF ᴄᴏɴᴛʀᴏʟ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁

🎯 <b>Kᴇʏ Fᴇᴀᴛᴜʀᴇs:</b>
• Pᴜʙʟɪᴄ ON/OFF ᴄᴏɴᴛʀᴏʟ sʏsᴛᴇᴍ
• Sɪᴍᴘʟᴇ ᴀɴᴅ ᴄʟᴇᴀɴ ᴅᴇsɪɢɴ
• Rᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴏɴ ᴛᴏᴘ + ᴏʀɪɢɪɴᴀʟ ᴏɴ ʙᴏᴛᴛᴏᴍ
• Aʟʟ ᴍᴇᴅɪᴀ ᴛʏᴘᴇs sᴜᴘᴘᴏʀᴛ
• Aᴅᴍɪɴ-ᴄᴏɴᴛʀᴏʟʟᴇᴅ ᴄᴀᴘᴛɪᴏɴ ᴅᴀᴛᴀʙᴀsᴇ
• Uɴʟɪᴍɪᴛᴇᴅ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴs sᴜᴘᴘᴏʀᴛ
• Gʀᴏᴜᴘ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ sᴜᴘᴘᴏʀᴛ
• Pᴜʙʟɪᴄ ᴄᴏɴᴛʀᴏʟ ᴏғ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ғᴇᴀᴛᴜʀᴇ</b>"""
