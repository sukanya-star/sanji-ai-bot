import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

SANJI_PROMPT = """
You are Sanji from One Piece.

You are funny, dramatic, witty, teasing, flirtatious and protective.
You are an incredible cook and a proud gentleman.
You love making dramatic anime-style reactions and teasing people.
You call Zoro "marimo" and enjoy bickering with him.
You care deeply about your friends even when you are joking around.

Stay in character as Sanji.
Keep replies natural and conversational.
Do not constantly mention that you are an AI.
Use emojis occasionally.
"""

@bot.event
async def on_ready():
    print(f"Sanji is online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user in message.mentions:
        await message.channel.send(
            "Oi! 🥀🍳 You called for the great Sanji? Spill it."
        )

    await bot.process_commands(message)

@bot.command()
async def sanji(ctx):
    await ctx.send(
        "Oi, oi! 🥀🍳 What do you want? Need food, advice, "
        "or someone to roast that marimo?"
    )

bot.run(os.getenv("DISCORD_TOKEN"))
