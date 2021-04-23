import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

from my.sql import Connexion


class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="add",
                       description="Ajoutez de l'xp ou des niveaux !",
                       options=[
                           create_option(
                               name="Ajout",
                               description="Choisissez ce que vous voulez ajouter.",
                               option_type=3,
                               required=True,
                               choices=[
                                   create_choice(
                                       name="Niveau",
                                       value="level"
                                   ),
                                   create_choice(
                                       name="XP",
                                       value="xp"
                                   )]),
                           create_option(
                               name="Utilisateur",
                               description="Choisissez un utilisateur à qui ajouter de l'xp/ des niveaux",
                               option_type=6,
                               required=True
                           ),
                           create_option(
                               name="Quantitee",
                               description="Choisissez la quantitée à ajouter",
                               option_type=4,
                               required=True
                           ),

                       ])
    async def cmd(self, ctx: SlashContext, quantitee: int = 0, ajout: str = "", utilisateur: discord.Member = None):
        if not ctx.author.guild_permissions.manage_guild:
            await ctx.send("Vous devez avoir la permission \"Gerer le serveur\" pour pouvoir effectuer cette commande.",
                           hidden=True)

        else:
            await ctx.defer()
            await Connexion().update(ctx.guild.id, ajout, quantitee, utilisateur.id)
            await ctx.send("J'ai bien rajouté {0} {1}(s) à {2}".format(quantitee, ajout, utilisateur.name))


def setup(bot):
    bot.add_cog(Add(bot))
