import motor.motor_asyncio
from Bot.config import MONGO_URL


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

db = client["FrierenzBot"]

db.Users = db["Users"]