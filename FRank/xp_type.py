from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

from my.sql import Connexion


class Schannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_subcommand(base="option", name="type",
                            description="Selectionez quelles actions ajoutent de l'xp",
                            options=[create_option(
                                name="type",
                                description="Quelle(s) actions ajouterons de l'xp",
                                option_type=3,
                                choices=[
                                    create_choice(name="Messages",
                                                  value="0"),
                                    create_choice(name="Vocal",
                                                  value="1"),
                                    create_choice(name="Mixte",
                                                  value="2")
                                ],
                                required=True
                            )])
    async def _set_type(self, ctx: SlashContext, type: str = None):
        type = int(type)
        if not ctx.author.guild_permissions.manage_guild:
            await ctx.send("Vous devez avoir la permission \"Gerer le serveur\" pour pouvoir effectuer cette commande.",
                           hidden=True)
        else:
            await ctx.defer()

            # 0 = messages only

            # 1 = voice only

            # 2 = voice & messages

            await Connexion().set_type(type, ctx.guild.id)

            sentences = ["quand un message est envoyé", "en fonction du temps passé dans un salon vocal", "quand un message est envoyé et en fonction du temps passé dans un salon vocal"]
            await ctx.send("De l'xp sera désormais donné " + sentences[type])


def setup(bot):
    bot.add_cog(Schannel(bot))
