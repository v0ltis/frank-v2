import discord
from discord.ext import commands

import my.sql


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if not ctx.author.bot and type(ctx.channel) == discord.TextChannel:
            await my.sql.Connexion().add_xp(ctx.author.id, ctx.guild.id, self.bot, ctx.channel.id)

    @commands.Cog.listener()
    async def on_ready(self):
        print("En ligne !")

    @staticmethod
    @commands.Cog.listener()
    async def on_command_error(ctx, error):

        raise error

    @staticmethod
    @commands.Cog.listener()
    async def on_error(ctx, error):
        if not (isinstance(error, commands.CommandNotFound) or isinstance(error, discord.Forbidden)):
            print("</---------------\\")
            print(ctx)
            print(error)
            print("\\<===============>/")


def setup(bot):
    bot.add_cog(Events(bot))
