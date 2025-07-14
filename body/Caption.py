from pyrogram import *
from info import *
import asyncio
from Script import script
from .database import *
import re
import sys
import time
import os
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

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["total_users"]))
async def all_db_users_here(client, message):
    silicon = await message.reply_text("Please Wait....")
    silicon_botz = await total_user()
    try:
        enabled_users = await total_enabled_users()
        disabled_users = await total_disabled_users()
        filter_users = await total_users_with_filters()
        await silicon.edit(f"**📊 User Statistics:**\n\n• Total Users: `{silicon_botz}`\n• Bot Enabled: `{enabled_users}`\n• Bot Disabled: `{disabled_users}`\n• Users with Filters: `{filter_users}`")
    except:
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
                deactivated += 1
                await delete({"_id": user['_id']})
            except errors.UserIsBlocked:
                blocked += 1
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

@Client.on_message(filters.command("bot_on"))
async def bot_on_cmd(bot, message):
    user_id = message.from_user.id
    
    # For channel/group messages, also set for the chat
    if message.chat.type in ['channel', 'supergroup']:
        chat_id = message.chat.id
        await set_user_bot_status(chat_id, True)
    
    success = await set_user_bot_status(user_id, True)
    if success:
        await message.reply("**✅ Bot is now ON for you!**\n\nAutomatic caption feature is **ENABLED** for your account. Bot will add random captions to your media posts.")
    else:
        await message.reply("**❌ Failed to turn ON the bot for you. Please try again.**")

@Client.on_message(filters.command("bot_off"))
async def bot_off_cmd(bot, message):
    user_id = message.from_user.id
    
    # For channel/group messages, also set for the chat
    if message.chat.type in ['channel', 'supergroup']:
        chat_id = message.chat.id
        await set_user_bot_status(chat_id, False)
    
    success = await set_user_bot_status(user_id, False)
    if success:
        await message.reply("**🔴 Bot is now OFF for you!**\n\nAutomatic caption feature is **DISABLED** for your account. Bot will not modify your captions.")
    else:
        await message.reply("**❌ Failed to turn OFF the bot for you. Please try again.**")

@Client.on_message(filters.command("bot_status"))
async def bot_status_cmd(bot, message):
    user_id = message.from_user.id
    status = await get_user_bot_status(user_id)
    
    # Also check channel/group status
    if message.chat.type in ['channel', 'supergroup']:
        chat_status = await get_user_bot_status(message.chat.id)
        total_caps = await total_random_captions()
        
        if status and chat_status:
            status_text = f"**🟢 Bot Status: ON**\n\n✅ Both user and chat have bot **ENABLED**\n📊 Total Random Captions: `{total_caps}`"
        elif status:
            status_text = f"**🟡 Bot Status: PARTIAL**\n\n✅ User: **ENABLED**\n❌ Chat: **DISABLED**\n📊 Total Random Captions: `{total_caps}`"
        elif chat_status:
            status_text = f"**🟡 Bot Status: PARTIAL**\n\n❌ User: **DISABLED**\n✅ Chat: **ENABLED**\n📊 Total Random Captions: `{total_caps}`"
        else:
            status_text = f"**🔴 Bot Status: OFF**\n\n❌ Both user and chat have bot **DISABLED**\n📊 Total Random Captions: `{total_caps}`"
    else:
        total_caps = await total_random_captions()
        if status:
            status_text = f"**🟢 Your Bot Status: ON**\n\n✅ Automatic caption feature is **ENABLED**\n📊 Total Random Captions: `{total_caps}`"
        else:
            status_text = f"**🔴 Your Bot Status: OFF**\n\n❌ Automatic caption feature is **DISABLED**\n📊 Total Random Captions: `{total_caps}`"
    
    await message.reply(status_text)

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
        
        if len(caption_text) > 3500:
            await loading.edit(caption_text)
            caption_text = ""
            loading = await message.reply("**More captions...**")
    
    if caption_text:
        await loading.edit(caption_text)

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("total_captions"))
async def admin_total_captions_cmd(bot, message):
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
    
    preview_text = "**📝 Random Captions Preview (First 10):**\n\n"
    for i, caption in enumerate(captions[:10], 1):
        caption_content = caption['caption'][:60] + "..." if len(caption['caption']) > 60 else caption['caption']
        preview_text += f"**{i}.** {caption_content}\n\n"
    
    preview_text += f"**Total Captions Available:** `{len(captions)}`"
    await loading.edit(preview_text)

@Client.on_message(filters.command("del"))
async def del_words_cmd(bot, message):
    user_id = message.from_user.id
    
    if len(message.command) < 2:
        return await message.reply("**Usage:** `/del word1, word2, word3`\n\n**Example:** `/del alok, spam, delete`")
    
    words_text = message.text.split(" ", 1)[1]
    words = [word.strip() for word in words_text.split(",")]
    
    words = [word for word in words if word]
    
    if not words:
        return await message.reply("**❌ No valid words found!**\n\n**Usage:** `/del word1, word2, word3`")
    
    success = await add_user_filter(user_id, words)
    
    if success:
        words_str = ", ".join(words)
        await message.reply(f"**✅ Words added to filter successfully!**\n\n**Filtered Words:** {words_str}\n\n**Note:** These words will be removed from your captions automatically.")
    else:
        await message.reply("**❌ Failed to add words to filter. Please try again.**")

@Client.on_message(filters.command("del_list"))
async def del_list_cmd(bot, message):
    user_id = message.from_user.id
    filtered_words = await get_user_filters(user_id)
    
    if not filtered_words:
        await message.reply("**📝 No filtered words found!**\n\nUse `/del word1, word2` to add words to filter.")
    else:
        words_str = ", ".join(filtered_words)
        await message.reply(f"**📝 Your Filtered Words:**\n\n{words_str}\n\n**Note:** These words are automatically removed from your captions.")

@Client.on_message(filters.command("del_clear"))
async def del_clear_cmd(bot, message):
    user_id = message.from_user.id
    success = await clear_user_filters(user_id)
    
    if success:
        await message.reply("**✅ All filtered words cleared successfully!**\n\nNo words will be removed from your captions now.")
    else:
        await message.reply("**❌ Failed to clear filtered words. Please try again.**")

@Client.on_message(filters.channel | filters.group)
async def reCap(bot, message):
    try:
        user_id = None
        if message.from_user:
            user_id = message.from_user.id
        elif message.sender_chat:
            user_id = message.sender_chat.id
        else:
            user_id = message.chat.id
        
        # Check if bot is enabled for this user/channel
        if user_id:
            try:
                user_bot_enabled = await get_user_bot_status(user_id)
                if not user_bot_enabled:
                    return  # Bot is OFF for this user, don't process
            except Exception as e:
                pass
        
        default_caption = message.caption or ""
        
        # Get user's filtered words
        filtered_words = []
        if user_id:
            try:
                filtered_words = await get_user_filters(user_id)
            except Exception as e:
                pass
        
        # Check if message has media
        media_found = False
        
        if message.photo:
            media_found = True
        elif message.video:
            media_found = True
        elif message.audio:
            media_found = True
        elif message.document:
            media_found = True
        elif message.voice:
            media_found = True
        elif message.video_note:
            media_found = True
        elif message.animation:
            media_found = True
        elif message.sticker:
            media_found = True
        
        if media_found:
            # Get random caption from database
            random_caption = await get_random_caption()
            
            if random_caption:
                # Apply word filters to BOTH random caption and original caption
                if filtered_words:
                    random_caption = remove_filtered_words(random_caption, filtered_words)
                    default_caption = remove_filtered_words(default_caption, filtered_words)
                
                # Combine captions
                if default_caption:
                    final_caption = f"{random_caption}\n\n{default_caption}"
                else:
                    final_caption = random_caption
                
                # Edit the message with new caption
                await message.edit_caption(final_caption)
            
    except FloodWait as e:
        await asyncio.sleep(e.x)
    except Exception as e:
        pass

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
                InlineKeyboardButton('Help', callback_data='help')
            ],[
                InlineKeyboardButton('↩ ʙᴀᴄᴋ', callback_data='start')
            ]]
        ),
        disable_web_page_preview=True
    )
