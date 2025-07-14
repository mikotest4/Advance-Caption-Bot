from pyrogram import Client, filters
from info import *
import asyncio
from Script import script
from .database import *
import re
import sys
import time
import os
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import errors

@Client.on_message(filters.command("start") & filters.private)
async def strtCap(bot, message):
    user_id = int(message.from_user.id)
    await insert(user_id)
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ʏ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ᴀ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ᴇ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ᴍ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ɪ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ᴋ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ᴏ", url="https://t.me/Yae_X_Miko")
            ],
            [
                InlineKeyboardButton("ᴍᴀᴋᴇ ᴍᴇ ʏᴏᴜʀ", url="https://t.me/Testmikosbot?startchannel=true"),
                InlineKeyboardButton("ᴍʏ ᴍᴀsᴛᴇʀ", url="https://t.me/Yae_X_Miko")
            ]
        ]
    )
    caption = f"""<b>🎊 ʙᴏᴛ ᴡᴇʟᴄᴏᴍᴇs ʏᴏᴜ 🎊

ʜᴇʟʟᴏ {message.from_user.mention}! ʀᴇᴀᴅʏ ᴛᴏ ᴇᴅɪᴛ ᴄᴀᴘᴛɪᴏɴ? 😉

ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ, ᴀɴᴅ ᴛʜɪs ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴜʀɴ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴs ɪɴᴛᴏ ʙᴇᴛᴛᴇʀ ᴏɴᴇs ⚡️

ᴛʜɪs ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴍʏ ᴍᴀsᴛᴇʀ – sᴀʏ ᴛʜᴀɴᴋs ᴛᴏ ʜɪᴍ 🙏</b>"""
    await message.reply_photo(
        photo=START_PIC,
        caption=caption,
        reply_markup=keyboard
    )

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["total_users"]))
async def all_db_users_here(client, message):
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

@Client.on_message(filters.command("bot_on"))
async def bot_on_cmd(bot, message):
    chat_id = message.chat.id
    await set_bot_status(chat_id, True)
    await message.reply("**✅ Bot is now ON! Random captions will be added to media posts.**")

@Client.on_message(filters.command("bot_off"))
async def bot_off_cmd(bot, message):
    chat_id = message.chat.id
    await set_bot_status(chat_id, False)
    await message.reply("**❌ Bot is now OFF! Random captions will not be added.**")

@Client.on_message(filters.command("bot_status"))
async def bot_status_cmd(bot, message):
    chat_id = message.chat.id
    status = await get_bot_status(chat_id)
    status_text = "**ON** ✅" if status else "**OFF** ❌"
    await message.reply(f"**🤖 Bot Status:** {status_text}")

# Enhanced media group handling with database storage
@Client.on_message(filters.channel | filters.group)
async def reCap(bot, message):
    try:
        # Check if bot is enabled for this chat
        chat_id = message.chat.id
        bot_enabled = await get_bot_status(chat_id)
        if not bot_enabled:
            return

        default_caption = message.caption or ""
        media_found = False
        
        # Check for media types
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
            # Handle media groups with database storage
            if message.media_group_id:
                # Add small delay to ensure we get the first message in the group
                await asyncio.sleep(0.5)
                
                # Check if this media group is already processed
                is_processed = await is_media_group_processed(message.media_group_id)
                
                if not is_processed:
                    # Mark this media group as processed
                    await mark_media_group_processed(message.media_group_id)
                    
                    # Get random caption and apply it
                    random_caption = await get_random_caption()
                    if random_caption:
                        bold_random_caption = f"<b>{random_caption}</b>"
                        if default_caption:
                            bold_default_caption = f"<b>{default_caption}</b>"
                            final_caption = f"{bold_random_caption}\n\n{bold_default_caption}"
                        else:
                            final_caption = bold_random_caption
                        
                        try:
                            await message.edit_caption(final_caption)
                        except Exception as e:
                            print(f"Error editing caption: {e}")
                            pass
                # If already processed, do nothing (this ensures only first photo gets caption)
            else:
                # Handle single media (not in a group)
                random_caption = await get_random_caption()
                if random_caption:
                    bold_random_caption = f"<b>{random_caption}</b>"
                    if default_caption:
                        bold_default_caption = f"<b>{default_caption}</b>"
                        final_caption = f"{bold_random_caption}\n\n{bold_default_caption}"
                    else:
                        final_caption = bold_random_caption
                    
                    try:
                        await message.edit_caption(final_caption)
                    except Exception as e:
                        print(f"Error editing caption: {e}")
                        pass
                        
    except FloodWait as e:
        await asyncio.sleep(e.x)
    except Exception as e:
        print(f"Error in reCap: {e}")
        pass

# Cleanup old media group records (run periodically)
@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("cleanup_media_groups"))
async def cleanup_media_groups_cmd(bot, message):
    await cleanup_old_media_groups()
    await message.reply("**✅ Old media group records cleaned up successfully!**")
