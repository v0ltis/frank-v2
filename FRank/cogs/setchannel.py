import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

from my.sql import Connexion


class Schannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_subcommand(base="option", name="annonce",
                            description="Selectionez où seront annoncés les levels-ups !",
                            options=[create_option(
                                name="Salon",
                                description="Les levels-ups seront annoncés dans ce salon. Laissez vide pour reinitialiser.",
                                option_type=7,
                                required=False
                            )])
    async def _anouncement(self, ctx: SlashContext, salon: discord.TextChannel = None):
        if not ctx.author.guild_permissions.manage_channels:
            await ctx.send("Vous devez avoir la permission \"Gerer les salons\" pour pouvoir effectuer cette commande.",
                           hidden=True)

        elif type(salon) != discord.TextChannel and salon is not None:
            await ctx.send("Veulliez selectioner un salon textuel.", hidden=True)
        else:
            await ctx.defer()
            if salon is None:
                await ctx.send("Très bien, le salon d'annonce a été reinitialisé")
            else:
                await ctx.send("Très bien, le salon d'annonce est désormais <#{}>".format(salon.id))
                salon = salon.id

            await Connexion().setchannel(ctx.guild.id, salon)


def setup(bot):
    bot.add_cog(Schannel(bot))
