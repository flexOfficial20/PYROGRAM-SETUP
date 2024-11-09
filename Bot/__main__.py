import asyncio
import importlib
import os
from Bot.modules import MODULES_PATH
from Bot.callbacks import CALLBACKS_PATH
from Bot.decorators import DECORATORS_PATH
from rich.console import Console
from pyrogram import idle
from typing import List

LOG = Console()
loop = asyncio.get_event_loop()

async def load_modules(paths: List[str], module_type: str) -> None:
    """Load all modules from a given path list, logging each loaded module."""
    LOG.print(f"[bold yellow]Loading {len(paths)} {module_type} Modules")
    for path in paths:
        try:
            module_name = os.path.relpath(path, os.getcwd()).replace(os.sep, '.').replace(".py", '')
            LOG.print(f"[bold cyan]{module_name.split('.')[-1]}")
            importlib.import_module(module_name)
        except Exception as e:
            LOG.print(f"[bold red]Failed to load {module_name}: {e}")

async def main() -> None:
    """Main function to load all modules and start the bot."""
    await load_modules(MODULES_PATH, "Bot")
    await load_modules(CALLBACKS_PATH, "Callback")
    await load_modules(DECORATORS_PATH, "Decorator")
    
    LOG.print("✨ [bold green]Bot started")
    await idle()
    LOG.print("🚫 [bold red]Bot stopping. Cancelling all tasks.")

if __name__ == "__main__":
    loop.run_until_complete(main())
