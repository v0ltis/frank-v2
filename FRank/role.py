import json

import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option

from my.sql import Connexion


class Rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_subcommand(base="option", subcommand_group="roles", name="ajouter",
                            description="Ajoutez un role donné en fonction du niveau",
                            options=[create_option(
                                name="Role",
                                description="Le rôle à donner",
                                option_type=8,
                                required=True),

                                create_option(
                                    name="Niveau",
                                    description="À quel niveau donner le role ?",
                                    option_type=4,
                                    required=True)])
    async def add_role(self, ctx, role: discord.Role, niveau: int):
        if not ctx.author.guild_permissions.manage_roles:
            await ctx.send("Vous devez avoir la permission \"Gerer les roles\" pour pouvoir effectuer cette commande.",
                           hidden=True)
        else:
            await ctx.defer()
            await Connexion().add_role(role.id, ctx.guild.id, niveau)

            await ctx.send(
                "{0} sera désormais donné quand quelqu'un depasse le niveau {1} !".format(role.mention, niveau),
                allowed_mentions=discord.AllowedMentions().none())

    @cog_ext.cog_subcommand(base="option", subcommand_group="roles", name="supprimer",
                            description="Ajoutez un role donné en fonction du niveau",
                            options=[create_option(
                                name="Role",
                                description="Le rôle à supprimer",
                                option_type=8,
                                required=True)])
    async def del_role(self, ctx, role: discord.Role):
        if not ctx.author.guild_permissions.manage_roles:
            await ctx.send("Vous devez avoir la permission \"Gerer les roles\" pour pouvoir effectuer cette commande.",
                           hidden=True)
        else:
            await ctx.defer()
            resp = await Connexion().del_role(ctx.guild.id, role.id)

            if resp:
                await ctx.send("Le role {0} ne sera désormais plus donné.".format(role.mention),
                               allowed_mentions=discord.AllowedMentions().none())
            else:
                await ctx.send("Ce role n'est pas donné lors de levels-up, impossible de le supprimer.")

    @cog_ext.cog_subcommand(base="option", subcommand_group="roles", subcommand_group_description="Modifiez les paramètres des roles", name="liste",
                            description="Affiche les roles donnés en fonction des niveaux")
    async def get_roles(self, ctx):
        await ctx.defer(True)
        data = await Connexion().list_roles(ctx.guild.id)

        if data == [] or len(json.loads(data[0][1])) == 0:
            await ctx.send("Il n'y a pour le moment auccun roles d'activés.", hidden=True)

        else:
            message = ""
            data = json.loads(data[0][1])
            for x in data:
                message += "Niveau {}: <@&{}>\n".format(x, data[x])
            await ctx.send(message, hidden=True)


def setup(bot):
    bot.add_cog(Rank(bot))
