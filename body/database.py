import motor.motor_asyncio
from info import *
import random
from datetime import datetime, timedelta

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
db = client.captions_with_chnl
users = db.users
random_captions = db.random_captions
bot_status = db.bot_status
processed_media_groups = db.processed_media_groups

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

# Random Caption Functions
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
        
        random_skip = random.randint(0, total_captions - 1)
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

# Bot Status Functions
async def set_bot_status(chat_id, status):
    """Set bot status for a chat"""
    await bot_status.update_one(
        {"chat_id": chat_id},
        {"$set": {"status": status, "updated_at": datetime.utcnow()}},
        upsert=True
    )

async def get_bot_status(chat_id):
    """Get bot status for a chat (default is True)"""
    result = await bot_status.find_one({"chat_id": chat_id})
    return result.get("status", True) if result else True

async def get_all_bot_statuses():
    """Get all bot statuses for admin"""
    statuses = []
    async for status in bot_status.find({}):
        statuses.append(status)
    return statuses

# Media Group Tracking Functions
async def mark_media_group_processed(media_group_id):
    """Mark a media group as processed"""
    try:
        await processed_media_groups.insert_one({
            "media_group_id": media_group_id,
            "processed_at": datetime.utcnow()
        })
        return True
    except Exception as e:
        print(f"Error marking media group as processed: {e}")
        return False

async def is_media_group_processed(media_group_id):
    """Check if a media group is already processed"""
    try:
        result = await processed_media_groups.find_one({"media_group_id": media_group_id})
        return result is not None
    except Exception as e:
        print(f"Error checking media group status: {e}")
        return False

async def cleanup_old_media_groups():
    """Clean up media group records older than 1 hour"""
    try:
        one_hour_ago = datetime.utcnow() - timedelta(hours=1)
        result = await processed_media_groups.delete_many({"processed_at": {"$lt": one_hour_ago}})
        return result.deleted_count
    except Exception as e:
        print(f"Error cleaning up old media groups: {e}")
        return 0

async def get_processed_media_groups_count():
    """Get total count of processed media groups"""
    try:
        count = await processed_media_groups.count_documents({})
        return count
    except Exception as e:
        print(f"Error getting processed media groups count: {e}")
        return 0

# Advanced Caption Functions
async def get_random_caption_with_stats():
    """Get a random caption and update its usage stats"""
    try:
        total_captions = await random_captions.count_documents({})
        if total_captions == 0:
            return None
        
        random_skip = random.randint(0, total_captions - 1)
        cursor = random_captions.find({}).skip(random_skip).limit(1)
        random_caption_doc = await cursor.to_list(length=1)
        
        if random_caption_doc:
            caption_id = random_caption_doc[0]['_id']
            caption_text = random_caption_doc[0]['caption']
            
            # Update usage count
            await random_captions.update_one(
                {"_id": caption_id},
                {
                    "$inc": {"usage_count": 1},
                    "$set": {"last_used": datetime.utcnow()}
                }
            )
            
            return caption_text
        else:
            return None
    except Exception as e:
        print(f"Error getting random caption with stats: {e}")
        return None

async def get_caption_stats():
    """Get statistics about caption usage"""
    try:
        total_captions = await random_captions.count_documents({})
        most_used_cursor = random_captions.find({}).sort("usage_count", -1).limit(5)
        most_used = await most_used_cursor.to_list(length=5)
        
        least_used_cursor = random_captions.find({}).sort("usage_count", 1).limit(5)
        least_used = await least_used_cursor.to_list(length=5)
        
        return {
            "total_captions": total_captions,
            "most_used": most_used,
            "least_used": least_used
        }
    except Exception as e:
        print(f"Error getting caption stats: {e}")
        return None

# Database Health Functions
async def get_database_health():
    """Get database health statistics"""
    try:
        stats = {
            "total_users": await users.count_documents({}),
            "total_captions": await random_captions.count_documents({}),
            "active_chats": await bot_status.count_documents({"status": True}),
            "processed_media_groups": await processed_media_groups.count_documents({}),
            "database_size": await get_database_size()
        }
        return stats
    except Exception as e:
        print(f"Error getting database health: {e}")
        return None

async def get_database_size():
    """Get approximate database size"""
    try:
        stats = await db.command("dbstats")
        return stats.get("dataSize", 0)
    except Exception as e:
        print(f"Error getting database size: {e}")
        return 0

# Bulk Operations
async def bulk_add_captions(captions_list):
    """Add multiple captions at once"""
    try:
        documents = [{"caption": caption, "added_at": datetime.utcnow()} for caption in captions_list]
        result = await random_captions.insert_many(documents)
        return len(result.inserted_ids)
    except Exception as e:
        print(f"Error bulk adding captions: {e}")
        return 0

async def export_captions():
    """Export all captions for backup"""
    try:
        captions = []
        async for caption in random_captions.find({}):
            captions.append({
                "id": str(caption["_id"]),
                "caption": caption["caption"],
                "usage_count": caption.get("usage_count", 0),
                "last_used": caption.get("last_used"),
                "added_at": caption.get("added_at")
            })
        return captions
    except Exception as e:
        print(f"Error exporting captions: {e}")
        return []

# Maintenance Functions
async def optimize_database():
    """Optimize database performance"""
    try:
        # Create indexes for better performance
        await random_captions.create_index("usage_count")
        await random_captions.create_index("last_used")
        await processed_media_groups.create_index("processed_at")
        await bot_status.create_index("chat_id")
        
        # Clean up old records
        cleanup_count = await cleanup_old_media_groups()
        
        return f"Database optimized. Cleaned up {cleanup_count} old records."
    except Exception as e:
        print(f"Error optimizing database: {e}")
        return f"Error optimizing database: {e}"

# Search Functions
async def search_captions(query):
    """Search captions by text"""
    try:
        captions = []
        async for caption in random_captions.find({
            "caption": {"$regex": query, "$options": "i"}
        }):
            captions.append(caption)
        return captions
    except Exception as e:
        print(f"Error searching captions: {e}")
        return []

async def get_recent_captions(limit=10):
    """Get recently added captions"""
    try:
        captions = []
        async for caption in random_captions.find({}).sort("added_at", -1).limit(limit):
            captions.append(caption)
        return captions
    except Exception as e:
        print(f"Error getting recent captions: {e}")
        return []

# Auto-cleanup function (can be called periodically)
async def auto_cleanup():
    """Automatic cleanup of old data"""
    try:
        # Clean up media groups older than 1 hour
        media_cleanup = await cleanup_old_media_groups()
        
        # Clean up unused bot status records older than 30 days
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)
        status_cleanup = await bot_status.delete_many({
            "updated_at": {"$lt": thirty_days_ago},
            "status": False
        })
        
        return {
            "media_groups_cleaned": media_cleanup,
            "status_records_cleaned": status_cleanup.deleted_count
        }
    except Exception as e:
        print(f"Error in auto cleanup: {e}")
        return {"error": str(e)}
