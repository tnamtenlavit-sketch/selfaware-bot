import discord
from discord.ext import commands, tasks
import asyncio
from aiohttp import web
import threading

# --- 1. TẠO WEB SERVER GIẢ LẬP ĐỂ GIỮ RENDER 24/24 ---
async def handle(request):
    return web.Response(text="Bot is active and running 24/7!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 10000)
    await site.start()

def run_server():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_web_server())
    loop.run_forever()

# Chạy web server ngầm trước khi bot khởi động
threading.Thread(target=run_server, daemon=True).start()
# --------------------------------------------------

# --- 2. CẤU HÌNH BOT DISCORD ---
intents = discord.Intents.default()
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

STATUS_LIST = [
    "Mood swings like the weather",
    "Body's under pressure",
    "Oh, I love the way you're using-",
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
    "But I'm way too self-aware"
]

async def change_status():
    await bot.wait_until_ready()
    while not bot.is_closed():
        for status in STATUS_LIST:
            await bot.change_presence(activity=discord.Game(name=status))
            await asyncio.sleep(4)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} đã kết nối thành công và bắt đầu chạy chữ!")
    bot.loop.create_task(change_status())

# --- 3. TOKEN CỦA BOT ---
bot.run("MTU0Mjg1ODExNzgxMTkyOTExOA.GQGjiX.noDFaxMKAtQ_rp4sMpw2oUpoItw8pEiIONerE4")