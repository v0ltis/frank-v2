import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

from my.sql import Connexion


class Delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="del", guild_ids=[658602051143598081],
                       description="Réinitialisez une personne",
                       options=[create_option(
                           name="Utilisateur",
                           description="Choisissez l'utilisateur à réinitialiser.",
                           option_type=6,
                           required=True
                       )])
    async def delete(self, ctx: SlashContext, utilisateur: discord.Member):
        resp = await Connexion().delete(utilisateur.id, ctx.guild.id)

        if not resp:
            await ctx.send("Désolé, cet utilisateur n'a pas été trouvé.", hidden=True)

        else:
            await ctx.send("L'utilisateur a bien été supprimé !")


def setup(bot):
    bot.add_cog(Delete(bot))
