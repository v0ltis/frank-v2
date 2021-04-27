import json

import discord

import my.sql


class Levelup:
    @staticmethod
    async def announce(bot, channel, user: int, level):
        try:
            channel = bot.get_channel(int(channel))
            await channel.send(":tada: Bravo <@{0}>, tu es passé niveau {1} :tada: !".format(user, level))
            g = channel.guild
            data = await my.sql.Connexion().list_roles(g.id)

            if not (data == [] or len(json.loads(data[0][1])) == 0):

                user = await g.fetch_member(user)
                data = json.loads(data[0][1])
                for x in data:
                    if int(x) <= int(level):
                        role = g.get_role(int(data[x]))

                        if role is not None:

                            try:
                                await user.add_roles(role)

                            except (discord.Forbidden, discord.HTTPException) as e:
                                print(e)
                                pass

        except discord.Forbidden:
            pass
