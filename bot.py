import discord
from discord.ext import commands, tasks
import asyncio

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

@tasks.loop(seconds=4)
async def change_status():
    for status in STATUS_LIST:
        await bot.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(4)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} đã kết nối thành công và bắt đầu chạy chữ!")
    change_status.start()

# Mã Token của bot (Thay TOKEN_MỚI vào giữa dấu ngoặc)
bot.run("MTU0Mjg1ODExNzgxMTkyOTExOA.GPSGx0.tv9V9DgldErZhVE8FGxuiyY1rO8TC1U0HDw15U")
