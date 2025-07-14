import motor.motor_asyncio
from info import *
import random
from datetime import datetime
import re

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
db = client.captions_with_chnl
users = db.users
random_captions = db.random_captions
user_settings = db.user_settings
user_filters = db.user_filters  # New collection for word filters

# User Functions
async def insert(user_id):
    user_det = {"_id": user_id}
    try:
        await users.insert_one(user_det)
    except:
        pass
        
async def total_user():
    user = await users.count_documents({})
    return user

async def getid():
    all_users = users.find({})
    return all_users

async def delete(id):
    await users.delete_one(id)

# User-Specific Bot Settings Functions
async def get_user_bot_status(user_id):
    """Get bot status for specific user"""
    try:
        user_setting = await user_settings.find_one({"_id": user_id})
        if user_setting:
            return user_setting.get("bot_enabled", True)  # Default is True (ON)
        else:
            # Create default setting for new user
            await user_settings.insert_one({
                "_id": user_id, 
                "bot_enabled": True,
                "created_at": datetime.now()
            })
            return True
    except Exception as e:
        print(f"Error getting user bot status: {e}")
        return True

async def set_user_bot_status(user_id, enabled):
    """Set bot status for specific user"""
    try:
        await user_settings.update_one(
            {"_id": user_id},
            {"$set": {
                "bot_enabled": enabled,
                "updated_at": datetime.now()
            }},
            upsert=True
        )
        return True
    except Exception as e:
        print(f"Error setting user bot status: {e}")
        return False

async def get_default_bot_status():
    """Get default bot status for new users"""
    return True  # Default is always ON for new users

# Old global functions kept for backward compatibility (if needed)
async def get_bot_status():
    """Get global bot status (deprecated - use get_user_bot_status instead)"""
    return True  # Always return True since we're using per-user settings now

async def set_bot_status(enabled):
    """Set global bot status (deprecated - use set_user_bot_status instead)"""
    return True  # Always return True since we're using per-user settings now

# Random Caption Functions (unchanged)
async def add_random_caption(caption_text):
    """Add a new random caption to database"""
    caption_data = {"caption": caption_text}
    await random_captions.insert_one(caption_data)

async def get_random_caption():
    """Get a random caption from database"""
    try:
        total_captions = await random_captions.count_documents({})
        if total_captions == 0:
            return None
        
        # Get random number between 0 and total_captions-1
        random_skip = random.randint(0, total_captions - 1)
        
        # Get random caption
        cursor = random_captions.find({}).skip(random_skip).limit(1)
        random_caption_doc = await cursor.to_list(length=1)
        
        if random_caption_doc:
            return random_caption_doc[0]['caption']
        else:
            return None
    except Exception as e:
        print(f"Error getting random caption: {e}")
        return None

async def delete_random_caption(caption_id):
    """Delete a random caption by ID"""
    from bson import ObjectId
    try:
        await random_captions.delete_one({"_id": ObjectId(caption_id)})
        return True
    except:
        return False

async def get_all_random_captions():
    """Get all random captions for listing"""
    captions = []
    async for caption in random_captions.find({}):
        captions.append(caption)
    return captions

async def total_random_captions():
    """Get total count of random captions"""
    count = await random_captions.count_documents({})
    return count

async def clear_all_random_captions():
    """Clear all random captions"""
    await random_captions.delete_many({})

# Additional helper functions for user settings
async def get_all_user_settings():
    """Get all user settings for admin purposes"""
    settings = []
    async for setting in user_settings.find({}):
        settings.append(setting)
    return settings

async def total_enabled_users():
    """Get count of users who have bot enabled"""
    count = await user_settings.count_documents({"bot_enabled": True})
    return count

async def total_disabled_users():
    """Get count of users who have bot disabled"""
    count = await user_settings.count_documents({"bot_enabled": False})
    return count

# NEW: User Filter Functions
async def add_user_filter(user_id, words):
    """Add filtered words for specific user"""
    try:
        # Convert words to lowercase for case-insensitive matching
        filtered_words = [word.strip().lower() for word in words if word.strip()]
        
        await user_filters.update_one(
            {"_id": user_id},
            {"$set": {
                "filtered_words": filtered_words,
                "updated_at": datetime.now()
            }},
            upsert=True
        )
        return True
    except Exception as e:
        print(f"Error adding user filter: {e}")
        return False

async def get_user_filters(user_id):
    """Get filtered words for specific user"""
    try:
        user_filter = await user_filters.find_one({"_id": user_id})
        if user_filter:
            return user_filter.get("filtered_words", [])
        else:
            return []
    except Exception as e:
        print(f"Error getting user filters: {e}")
        return []

async def clear_user_filters(user_id):
    """Clear all filtered words for specific user"""
    try:
        await user_filters.delete_one({"_id": user_id})
        return True
    except Exception as e:
        print(f"Error clearing user filters: {e}")
        return False

def remove_filtered_words(text, filtered_words):
    """Remove filtered words from text"""
    if not text or not filtered_words:
        return text
    
    # Create a copy of the text
    cleaned_text = text
    
    # Remove each filtered word (case-insensitive)
    for word in filtered_words:
        # Use regex to remove the word (whole word matching)
        pattern = r'\b' + re.escape(word) + r'\b'
        cleaned_text = re.sub(pattern, '', cleaned_text, flags=re.IGNORECASE)
    
    # Clean up extra spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

async def total_users_with_filters():
    """Get count of users who have word filters set"""
    count = await user_filters.count_documents({})
    return count
