from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option

from my.sql import Connexion


class Reset(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="reset", guild_ids=[658602051143598081],
                       description="Reinitalise tout les utilisateurs",
                       options=[create_option(
                           name="Confirmation",
                           description="Veuillez confirmer",
                           option_type=5,
                           required=True
                       )])
    async def reset(self, ctx, confirmation: bool = False):
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("Vous devez avoir la permission \"Administrateur\" pour pouvoir effectuer cette commande.",
                           hidden=True)
        elif not confirmation:
            await ctx.send("Annulé", hidden=True)
        else:
            await Connexion().reset(ctx.guild.id)
            await ctx.send("La reinitalisation a bien été effectué.")


def setup(bot):
    bot.add_cog(Reset(bot))
