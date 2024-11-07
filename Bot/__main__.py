import asyncio
import importlib
import os

from Bot.handlers import MODULES_PATH
from rich.console import Console
from pyrogram import idle

loop = asyncio.get_event_loop()
IMPORTED = {}


LOG = Console()

async def main():
    # from .modules.waifu_dropper import character_cache
    LOG.print(f"[bold yellow]Loading {len(MODULES_PATH)} Modules")
    for module in MODULES_PATH:
        mod = module.replace(os.getcwd(),"")[1:].replace('/','.').replace(".py",'')
        LOG.print(f"[bold cyan]{mod.split('.')[-1]}")
        
        importlib.import_module(mod)
         
    print("✨ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ")
    await idle()
    print("ᴄᴀɴᴄᴇʟɪɴɢ ᴀʟʟ ᴛᴀsᴋs.")


if __name__ == "__main__":
    loop.run_until_complete(main())
    
