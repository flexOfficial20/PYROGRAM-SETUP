from pyrogram import Client, filters
from Bot import app

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(f"Hello {message.from_user.first_name}! 👋\nWelcome to the bot.")
