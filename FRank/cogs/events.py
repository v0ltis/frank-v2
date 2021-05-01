import discord
from discord.ext import commands, tasks

import my.sql


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.con = my.sql.Connexion

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if not ctx.author.bot and type(ctx.channel) == discord.TextChannel:
            if int((await self.con().get(ctx.guild.id))[3]) in {0, 2}:
                await self.con().add_xp(ctx.author.id, ctx.guild.id, self.bot, ctx.channel.id)

    @commands.Cog.listener()
    async def on_ready(self):
        print("En ligne !")
        self.voice_xp.start()
        await self.bot.change_presence(activity=discord.Streaming(name="de l'xp", type=discord.ActivityType.watching, url="https://www.twitch.tv/discord"), status=discord.Status.dnd)

    @staticmethod
    @commands.Cog.listener()
    async def on_command_error(ctx, error):

        raise error

    @staticmethod
    @commands.Cog.listener()
    async def on_slash_command_error(ctx, error):

        raise error

    @staticmethod
    @commands.Cog.listener()
    async def on_error(ctx, error):
        if not (isinstance(error, commands.errors.CommandNotFound) or isinstance(error, discord.errors.Forbidden)):
            print("</---------------\\")
            print(ctx)
            print(error)
            print("\\<===============>/")

    @tasks.loop(seconds=60)
    async def voice_xp(self):
        for guild in self.bot.guilds:
            if int((await self.con().get(guild.id))[3]) in {1, 2}:
                for channel in guild.voice_channels:
                    for user in channel.voice_states:
                        state = channel.voice_states[user]
                        if not (state.mute or state.self_mute or state.afk):
                            await self.con().add_xp(user, guild.id, self.bot, 0, voice=True)


def setup(bot):
    bot.add_cog(Events(bot))
