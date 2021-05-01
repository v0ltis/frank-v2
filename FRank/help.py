import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

chelp = discord.Embed(color=0xb42cfc)
chelp.add_field(name="@FRank help", value="Affiche l'aide", inline=False)
chelp.add_field(name="@FRank", value="Affiche vos statistiques", inline=False)
chelp.add_field(name="@FRank top", value="Affiche les 5 personnes les plus hautes dans le classement du serveur",
                inline=False)
chelp.add_field(name="Il manque des commandes ?",
                value="FRank utilise désomrais les slashs commands. Cliquez [ici](https://discord.com/oauth2/authorize?client_id=738341837395197952&permissions=0&scope=bot%20applications.commands) pour les activer sur votre serveur, et debloquer toutes les commandes !")
chelp.add_field(name="Besoin d'aide ?",
               value="> [Rejoignez notre serveur de support](https://discord.gg/F9f2KXG) !",
               inline=False)
chelp.add_field(name="Ajoutez FRank à votre serveur !",
                value="[en cliquant ici](https://discord.com/oauth2/authorize?client_id=738341837395197952&scope=bot%20applications.commands&permissions=268749888)",
                inline=False)
chelp.set_footer(text="* Nécésite la permission \"Administrateur\" sur le serveur",
                 icon_url="https://cdn.discordapp.com/avatars/738341837395197952/e66f2b432f737429ab3e40c01a6ff7c9.png?size=256")

shelp = discord.Embed(color=0xb42cfc)
shelp.add_field(name="/help", value="Affiche l'aide", inline=False)
shelp.add_field(name="/stats (utilisateur)", value="Affiche les statistiques de vous ou de quelqu'un d'autre",
                inline=False)
shelp.add_field(name="/top", value="Affiche les 5 personnes les plus hautes dans le classement du serveur",
                inline=False)
shelp.add_field(name="/option [options] [paramètres]", value="Vous permet de modifier les options", inline=False)
shelp.add_field(name="/reset*", value="Réinitalise **tous** les stats du serveur", inline=False)
shelp.add_field(name="/del [utilisateur]*", value="Réinitalise l'xp d'une personne", inline=False)
shelp.add_field(name="/add [xp/niveau] [utilisateur] [quantitée]*", value="Ajoute des niveaux/xp à une personne.",
                inline=False)
shelp.add_field(name="Besoin d'aide ?",
               value="> [Rejoignez notre serveur de support](https://discord.gg/F9f2KXG) !",
               inline=False)
shelp.add_field(name="Ajoutez FRank à votre serveur !",
                value="[en cliquant ici](https://discord.com/oauth2/authorize?client_id=738341837395197952&scope=bot%20applications.commands&permissions=268749888)",
                inline=False)
shelp.set_footer(text="* Nécésite la permission \"Administrateur\" sur le serveur",
                 icon_url="https://cdn.discordapp.com/avatars/738341837395197952/e66f2b432f737429ab3e40c01a6ff7c9.png?size=256")


class Cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="help", description="Affiche les commandes")
    async def shelp(self, ctx: SlashContext):
        await ctx.send(embed=shelp, hidden=True)

    @commands.command(name="help")
    async def chelp(self, ctx: commands.context):
        await ctx.send(embed=chelp)


def setup(bot):
    bot.add_cog(Cmd(bot))
