from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(f"Hello {message.from_user.first_name}! 👋\nWelcome to the bot.")
