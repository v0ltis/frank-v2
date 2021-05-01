import discord
from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(help_command=None, command_prefix=["/", "<@738341837395197952> ", "<@!738341837395197952> "], intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)


exts = [
    "cogs.help",
    "cogs.info",
    "cogs.events",
    "cogs.setchannel",
    "cogs.add",
    "cogs.del",
    "cogs.role",
    "cogs.reset",
    "cogs.top",
    "cogs.cogs",
    "cogs.xp_type"
]

for ext in exts:
    bot.load_extension(ext)


bot.run("")
