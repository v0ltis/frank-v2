from discord.ext import commands


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="load")
    async def load(self, ctx, arg):
        if ctx.author.id == 362615539773997056:
            self.bot.load_extension(arg)
            await ctx.send("Cog chargé avec succès")

    @commands.command(name="reload")
    async def reload(self, ctx, arg):
        if ctx.author.id == 362615539773997056:
            self.bot.reload_extension(arg)
            await ctx.send("Cog rechargé avec succès")

    @commands.command(name="unload")
    async def unload(self, ctx, arg):
        if ctx.author.id == 362615539773997056:
            self.bot.unload_extension(arg)
            await ctx.send("Cog déchargé avec succès")


def setup(bot):
    bot.add_cog(Cog(bot))
