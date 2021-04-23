import json
from shutil import copyfile

import aiofiles
import aiohttp
import discord
from discord.ext import commands
from discord_slash import cog_ext

import my.sql as mysql
from image.img import Generator


class Top(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def global_top(ctx):
        levels = json.loads((await mysql.Connexion().get(ctx.guild.id))[1])

        if len(levels) >= 5:

            users = []
            for x in levels:
                users.append([x, levels[x]["level"], levels[x]["xp"]])

            def _cshort(e):
                return e[1], e[2]

            users.sort(key=_cshort, reverse=True)

            data = []

            for x in range(5):
                try:
                    user = await ctx.guild.fetch_member(int(users[x][0]))
                    db_user = users[x]

                    reqxp = round((((db_user[1] ** 2) + 50 + (db_user[1] * 10)) * 2.5))

                    data.append(
                        {"pseudo": user.name,
                         "couleur": user.color.to_rgb(),
                         "percent": db_user[2] * 100 / reqxp,
                         "level": db_user[1]})

                    async with aiohttp.ClientSession() as session:
                        url = str(user.avatar_url_as(format="png", static_format="png", size=512))
                        async with session.get(url) as resp:
                            f = await aiofiles.open('image/{}avatar.png'.format(x), mode='wb')
                            await f.write(await resp.read())
                            await f.close()
                except discord.errors.NotFound:
                    db_user = users[x]

                    reqxp = round((((db_user[1] ** 2) + 50 + (db_user[1] * 10)) * 2.5))
                    data.append({"pseudo": "Utilisateur",
                                 "couleur": (255, 255, 255),
                                 "percent": db_user[2] * 100 / reqxp,
                                 "level": db_user[1]})

                    copyfile("image/frank.png", "image/{}avatar.png".format(x))

            Generator.top(data)
            return True

    @cog_ext.cog_slash(name="top", guild_ids=[658602051143598081],
                       description="Affiche les 5 meilleurs membres du serveur")
    async def s_top(self, ctx):
        await ctx.defer()
        resp = await self.global_top(ctx)
        if resp:
            await ctx.send(file=discord.File("image/top.png"))
        else:
            await ctx.send("Désolé, il faut au moins 5 membres classés pour afficher le classement.")

    @commands.command(name="top")
    async def c_top(self, ctx):
        resp = await self.global_top(ctx)
        if resp:
            await ctx.send(file=discord.File("image/top.png"))
        else:
            await ctx.send("Désolé, il faut au moins 5 membres classés pour afficher le classement.")


def setup(bot):
    bot.add_cog(Top(bot))
