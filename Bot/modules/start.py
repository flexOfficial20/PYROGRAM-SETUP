from pyrogram import filters
from Bot import app


# Define the /start command
@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    await message.reply_text(
        f"Hello, {message.from_user.first_name}! 👋\n\n"
        "Welcome to our bot! Feel free to explore its features and ask for help if needed."
    )
