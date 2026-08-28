import discord
from discord.ext import commands, tasks
from aiohttp import web
import asyncio
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

STATUS_LIST = [
    "-your imagination",
    "Laws of attraction",
    "Put 'em into practice (Oh)",
    "Just don't hang your hopes on me",
    "I wanna feel something",
    "God, you look so pretty",
    "When you tell me that you love me",
    "I wish that I could lie",
    "But my mind gets in the way",
    "I know you think that I'm",
    "Always way too self-aware",
    "Oh, we could never be together",
    "But it's nice to play pretend",
    "I wish that I could lie",
    "But I'm way too self-aware",
    "Just don't hang your hopes on me",
    "I wanna feel something",
    "God, you look so pretty",
    "When you tell me that you love me (Oh)"
]

current_status_index = 0

@tasks.loop(seconds=4)
async def change_status():
    global current_status_index
    status = STATUS_LIST[current_status_index]
    await bot.change_presence(activity=discord.Game(name=status))
    current_status_index = (current_status_index + 1) % len(STATUS_LIST)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} đã kết nối thành công!")
    if not change_status.is_running():
        change_status.start()

# Web server giả để thông cổng PORT cho Render
async def handle(request):
    return web.Response(text="Bot online!")

async def start_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

async def main():
    async with bot:
        await start_server()
        await bot.start(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())
