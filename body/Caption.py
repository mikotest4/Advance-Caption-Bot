from pyrogram import *
from info import *
import asyncio
from Script import script
from .database import *
import re
import sys
import time
from pyrogram.errors import FloodWait
from pyrogram.types import *
from pyrogram import errors

@Client.on_message(filters.command("start") & filters.private)
async def strtCap(bot, message):
    user_id = int(message.from_user.id)
    await insert(user_id)
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️", url=f"https://t.me/CustomCaptionBot?startchannel=true")
            ],[
                InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
            ],[
                InlineKeyboardButton("🌐 Uᴘᴅᴀᴛᴇ", url=f"https://t.me/Silicon_Bot_Update"),
                InlineKeyboardButton("📜 Sᴜᴘᴘᴏʀᴛ", url=r"https://t.me/Silicon_Botz")
        ]]
    )
    await message.reply_photo(
        photo=SILICON_PIC,
        caption=f"<b>Hᴇʟʟᴏ {message.from_user.mention}\n\nɪ ᴀᴍ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ʀᴀɴᴅᴏᴍ ᴄᴀᴘᴛɪᴏɴ ꜰᴇᴀᴛᴜʀᴇ.\n\nFᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.\n\nMᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ »<a href='https://t.me/Silicon_Bot_Update'>Sɪʟɪᴄᴏɴ Bᴏᴛᴢ</a></b>",
        reply_markup=keyboard
    )

@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["total_users"]))
async def all_db_users_here(client,message):
    silicon = await message.reply_text("Please Wait....")
    silicon_botz = await total_user()
    await silicon.edit(f"Tᴏᴛᴀʟ Usᴇʀ :- `{silicon_botz}`")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
        silicon = await message.reply_text("Geting All ids from database..\n Please wait")
        all_users = await getid()
        tot = await total_user()
        success = 0
        failed = 0
        deactivated = 0
        blocked = 0
        await silicon.edit(f"ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ...")
        async for user in all_users:
            try:
                time.sleep(1)
                await message.reply_to_message.copy(user['_id'])
                success += 1
            except errors.InputUserDeactivated:
                deactivated +=1
                await delete({"_id": user['_id']})
            except errors.UserIsBlocked:
                blocked +=1
                await delete({"_id": user['_id']})
            except Exception as e:
                failed += 1
                await delete({"_id": user['_id']})
                pass
            try:
                await silicon.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴘʀᴏᴄᴇssɪɴɢ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
            except FloodWait as e:
                await asyncio.sleep(e.x)
        await silicon.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("restart"))
async def restart_bot(b, m):
    silicon = await b.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=m.chat.id)       
    await asyncio.sleep(3)
    await silicon.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)

# Original Caption Commands
@Client.on_message(filters.command("set_cap") & filters.channel)
async def setCap(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            "Usᴀɢᴇ: **/set_cap 𝑌𝑜𝑢𝑟 𝑐𝑎𝑝𝑡𝑖𝑜𝑛 𝑈𝑠𝑒 <code>{file_name}</code> 𝑇𝑜 𝑠ℎ𝑜𝑤 𝑦𝑜𝑢𝑟 𝐹𝑖𝑙𝑒 𝑁𝑎𝑚𝑒.\n\n𝑈𝑠𝑒<code>{file_size}</code> 𝑇𝑜 𝑠ℎ𝑜𝑤 𝑦𝑜𝑢𝑟 𝐹𝑖𝑙𝑒 𝑆𝑖𝑧𝑒/n/n✓ 𝑀𝑎𝑦 𝐵𝑒 𝑁𝑜𝑤 𝑌𝑜𝑢 𝑎𝑟𝑒 𝑐𝑙𝑒𝑎𝑟💫**"
        )
    chnl_id = message.chat.id
    caption = (
        message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    )
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chkData:
        await updateCap(chnl_id, caption)
        return await message.reply(f"Your New Caption: {caption}")
    else:
        await addCap(chnl_id, caption)
        return await message.reply(f"Yᴏᴜʀ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Is: {caption}")

@Client.on_message(filters.command("del_cap") & filters.channel)
async def delCap(_, msg):
    chnl_id = msg.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        return await msg.reply("<b><i>✓ Sᴜᴄᴄᴇssғᴜʟʟʏ... Dᴇʟᴇᴛᴇᴅ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Nᴏᴡ I ᴀᴍ Usɪɴɢ Mʏ Dᴇғᴀᴜʟᴛ Cᴀᴘᴛɪᴏɴ </i></b>")
    except Exception as e:
        e_val = await msg.reply(f"ERR I GOT: {e}")
        await asyncio.sleep(5)
        await e_val.delete()
        return

# Random Caption Commands - ONLY ADMIN CAN MANAGE
@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("add_caption"))
async def add_caption_cmd(bot, message):
    if len(message.command) < 2:
        return await message.reply("**Usage:** `/add_caption Your Random Caption Text`")
    
    caption_text = message.text.split(" ", 1)[1]
    await add_random_caption(caption_text)
    total_caps = await total_random_captions()
    await message.reply(f"**✅ Caption Added Successfully!**\n\n**Caption:** {caption_text}\n**Total Captions:** {total_caps}")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("list_captions"))
async def list_captions_cmd(bot, message):
    loading = await message.reply("**Getting all captions...**")
    captions = await get_all_random_captions()
    
    if not captions:
        return await loading.edit("**No random captions found!**")
    
    caption_text = "**📝 All Random Captions:**\n\n"
    for i, caption in enumerate(captions, 1):
        caption_id = str(caption['_id'])
        caption_content = caption['caption'][:50] + "..." if len(caption['caption']) > 50 else caption['caption']
        caption_text += f"**{i}.** `{caption_id}`\n{caption_content}\n\n"
        
        if len(caption_text) > 3500:  # Telegram message limit
            await loading.edit(caption_text)
            caption_text = ""
            loading = await message.reply("**More captions...**")
    
    if caption_text:
        await loading.edit(caption_text)

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("total_captions"))
async def total_captions_cmd(bot, message):
    total = await total_random_captions()
    await message.reply(f"**📊 Total Random Captions:** `{total}`")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("del_caption"))
async def del_caption_cmd(bot, message):
    if len(message.command) < 2:
        return await message.reply("**Usage:** `/del_caption caption_id`")
    
    caption_id = message.command[1]
    success = await delete_random_caption(caption_id)
    
    if success:
        total = await total_random_captions()
        await message.reply(f"**✅ Caption Deleted Successfully!**\n**Remaining Captions:** {total}")
    else:
        await message.reply("**❌ Failed to delete caption. Invalid ID or caption not found.**")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("clear_captions"))
async def clear_captions_cmd(bot, message):
    await clear_all_random_captions()
    await message.reply("**✅ All random captions cleared successfully!**")

# Public Commands - ANY USER CAN USE
@Client.on_message(filters.command("total_captions"))
async def public_total_captions(bot, message):
    total = await total_random_captions()
    await message.reply(f"**📊 Total Available Random Captions:** `{total}`")

@Client.on_message(filters.command("preview_captions"))
async def preview_captions_cmd(bot, message):
    loading = await message.reply("**Getting caption preview...**")
    captions = await get_all_random_captions()
    
    if not captions:
        return await loading.edit("**No random captions available!**")
    
    # Show only first 10 captions as preview
    preview_text = "**📝 Random Captions Preview (First 10):**\n\n"
    for i, caption in enumerate(captions[:10], 1):
        caption_content = caption['caption'][:60] + "..." if len(caption['caption']) > 60 else caption['caption']
        preview_text += f"**{i}.** {caption_content}\n\n"
    
    preview_text += f"**Total Captions Available:** `{len(captions)}`"
    await loading.edit(preview_text)

# Helper Functions
def extract_language(text):
    if not text:
        return "Hindi-English"
    language_pattern = r'\b(Hindi|English|Tamil|Telugu|Malayalam|Kannada|Hin|Eng|Tam|Tel|Mal|Kan)\b'
    languages = set(re.findall(language_pattern, text, re.IGNORECASE))
    if not languages:
        return "Hindi-English"
    return ", ".join(sorted(languages, key=str.lower))

def extract_year(text):
    if not text:
        return None
    match = re.search(r'\b(19\d{2}|20\d{2})\b', text)
    return match.group(1) if match else None

def get_file_info(media_obj):
    """Extract file information from media object"""
    file_info = {
        'name': 'Unknown',
        'size': 0,
        'type': 'Unknown'
    }
    
    if hasattr(media_obj, 'file_name') and media_obj.file_name:
        file_info['name'] = media_obj.file_name
    elif hasattr(media_obj, 'file_unique_id'):
        file_info['name'] = f"file_{media_obj.file_unique_id}"
    
    if hasattr(media_obj, 'file_size'):
        file_info['size'] = media_obj.file_size
    
    return file_info

# Main Caption Processing - AUTOMATIC FOR ALL USERS
@Client.on_message(filters.channel | filters.group)
async def reCap(bot, message):
    chnl_id = message.chat.id
    default_caption = message.caption or ""
    
    # Check if message has any media
    media_obj = None
    media_type = "Unknown"
    
    if message.photo:
        media_obj = message.photo
        media_type = "Photo"
    elif message.video:
        media_obj = message.video
        media_type = "Video"
    elif message.audio:
        media_obj = message.audio
        media_type = "Audio"
    elif message.document:
        media_obj = message.document
        media_type = "Document"
    elif message.voice:
        media_obj = message.voice
        media_type = "Voice"
    elif message.video_note:
        media_obj = message.video_note
        media_type = "Video Note"
    elif message.animation:
        media_obj = message.animation
        media_type = "GIF"
    elif message.sticker:
        media_obj = message.sticker
        media_type = "Sticker"
    
    # Process media if found
    if media_obj:
        try:
            # Extract file information
            file_info = get_file_info(media_obj)
            file_name = file_info['name']
            file_size = file_info['size']
            
            # Clean file name
            if file_name != 'Unknown':
                file_name = (
                    re.sub(r"@\w+\s*", "", file_name)
                    .replace("_", " ")
                    .replace(".", " ")
                )
            
            # Extract language and year
            language = extract_language(default_caption + " " + file_name)
            year = extract_year(default_caption + " " + file_name)
            
            # Get random caption from database - AUTOMATIC FOR ALL USERS
            random_caption = await get_random_caption()
            
            # Get channel specific caption or use default
            cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
            
            # Format file information
            file_info_text = ""
            if cap_dets:
                cap = cap_dets["caption"]
                file_info_text = cap.format(
                    file_name=file_name,
                    file_size=get_size(file_size),
                    default_caption=default_caption,
                    language=language,
                    year=year or "",
                    media_type=media_type
                )
            else:
                file_info_text = DEF_CAP.format(
                    file_name=file_name,
                    file_size=get_size(file_size),
                    default_caption=default_caption,
                    language=language,
                    year=year or "",
                    media_type=media_type
                )
            
            # Combine random caption with file info
            if random_caption:
                final_caption = f"{random_caption}\n\n{file_info_text}"
            else:
                final_caption = file_info_text
            
            # Edit the message with new caption
            await message.edit_caption(final_caption)
            
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception as e:
            print(f"Error processing media: {e}")
    
    return

# Size conversion function
def get_size(size):
    if size == 0:
        return "Unknown"
    
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units) - 1:
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

# Callback Query Handlers
@Client.on_callback_query(filters.regex(r'^start'))
async def start(bot, query):
    await query.message.edit_text(
        text=script.START_TXT.format(query.from_user.mention),  
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️", url=f"http://t.me/CustomCaptionBot?startchannel=true")
                ],[
                InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
            ],[
                InlineKeyboardButton("🌐 Uᴘᴅᴀᴛᴇ", url=f"https://t.me/Silicon_Bot_Update"),
                InlineKeyboardButton("📜 Sᴜᴘᴘᴏʀᴛ", url=r"https://t.me/Silicon_Botz")
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex(r'^help'))
async def help(bot, query):
    await query.message.edit_text(
        text=script.HELP_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('About', callback_data='about')
            ],[
            InlineKeyboardButton('↩ ʙᴀᴄᴋ', callback_data='start')
            ]]
        ),
        disable_web_page_preview=True    
    )

@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    await query.message.edit_text(
        text=script.ABOUT_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❓', callback_data='help')
            ],[
            InlineKeyboardButton('↩ ʙᴀᴄᴋ', callback_data='start')
            ]]
        ),
        disable_web_page_preview=True 
    )
