import discord
from discord import File
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
import aiohttp        
import aiofiles
from image.img import Generator
import my.sql as mysql
import json


class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def stats(self, ctx,user:discord.Member):
        data = await mysql.Connexion().get_user(user.id, user.guild.id)

        # niveau
        level = data['level']

        # telecharger image
        async with aiohttp.ClientSession() as session:
            url = str(user.avatar_url_as(format="png",static_format="png",size=1024))
            async with session.get(url) as resp:
                f = await aiofiles.open('image/avatar.png', mode='wb')
                await f.write(await resp.read())
                await f.close()

        # xp requis
        reqxp = round((((level ** 2) + 50 + (level*10)) * 2.5))

        # position
        levels = json.loads((await mysql.Connexion().get(user.guild.id))[1])

        users = []
        for x in levels:
            users.append([x, levels[x]["level"], levels[x]["xp"]])
        
        def CShort(e):
            return e[1], e[2]
        users.sort(key=CShort, reverse=True)

        pos = 0
        for x in users:
            pos +=1

            if str(x[0]) == str(user.id):
                break

        Generator.card(user.name, user.color.to_rgb(), data["xp"], reqxp, level, len(users), pos, ctx.guild.id)
        await ctx.send(file=File("image/level.png"))

    @cog_ext.cog_slash(name="stats",guild_ids =[658602051143598081], description="Affiche le niveaux et l'xp", 
    options=[create_option(
        name="Utilisateur",
        description="Les statistiques de cet utilisateur seront affichés",
        option_type = 6,
        required=False

    )])
    async def sstats(self, ctx: SlashContext, utilisateur: discord.member = None):
        await ctx.defer()
        if utilisateur is None:
            utilisateur = ctx.author
        await self.stats(ctx, utilisateur)

    @commands.command(name="stats")
    async def cstats(self, ctx:commands.context):
        await self.stats(ctx, ctx.author)     

def setup(bot):
    bot.add_cog(cmd(bot))