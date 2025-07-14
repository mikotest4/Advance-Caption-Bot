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

# Bot ON/OFF Commands - ONLY ADMIN
@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("bot_on"))
async def bot_on_cmd(bot, message):
    success = await set_bot_status(True)
    if success:
        await message.reply("**✅ Bot is now ON!**\n\nAutomatic caption feature is **ENABLED**. Bot will add random captions to all media posts.")
    else:
        await message.reply("**❌ Failed to turn ON the bot. Please try again.**")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("bot_off"))
async def bot_off_cmd(bot, message):
    success = await set_bot_status(False)
    if success:
        await message.reply("**🔴 Bot is now OFF!**\n\nAutomatic caption feature is **DISABLED**. Bot will not modify any captions.")
    else:
        await message.reply("**❌ Failed to turn OFF the bot. Please try again.**")

@Client.on_message(filters.command("bot_status"))
async def bot_status_cmd(bot, message):
    status = await get_bot_status()
    total_caps = await total_random_captions()
    
    if status:
        status_text = "**🟢 Bot Status: ON**\n\n✅ Automatic caption feature is **ENABLED**\n📊 Total Random Captions: `{}`".format(total_caps)
    else:
        status_text = "**🔴 Bot Status: OFF**\n\n❌ Automatic caption feature is **DISABLED**\n📊 Total Random Captions: `{}`".format(total_caps)
    
    await message.reply(status_text)

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

# Main Caption Processing - WITH ON/OFF CONTROL
@Client.on_message(filters.channel | filters.group)
async def reCap(bot, message):
    # Check if bot is enabled
    bot_enabled = await get_bot_status()
    if not bot_enabled:
        return  # Bot is OFF, don't process captions
    
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
            # Get random caption from database
            random_caption = await get_random_caption()
            
            # If random caption exists, combine it with original
            if random_caption:
                # Format: Random Caption + Original Caption
                if default_caption:
                    final_caption = f"{random_caption}\n\n{default_caption}"
                else:
                    final_caption = random_caption
                
                # Edit the message with new caption
                await message.edit_caption(final_caption)
            
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception as e:
            print(f"Error processing media: {e}")
    
    return

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
