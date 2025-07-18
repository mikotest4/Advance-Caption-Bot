import motor.motor_asyncio
from info import *
import random
from datetime import datetime

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
db = client.captions_with_chnl
users = db.users
random_captions = db.random_captions

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
