import json
import random

import mysql.connector

import cogs.levelup


class Connexion:
    def __init__(self):
        self.db = mysql.connector.connect(user='frank', password='frank',
                                          host='frank.frank',
                                          database='frank')

        self.cursor = self.db.cursor(buffered=True)

    async def add_user(self, guild: int, uid: int):
        req = "select * from users where guild = {} ".format(guild)
        self.cursor.execute(req)
        request = self.cursor.fetchall()

        if not request:
            insert = "insert into users VALUES ('{0}', '{{}}', null)".format(guild)
            self.cursor.execute(insert)
            self.db.commit()
            data = {}

        else:
            data = json.loads(request[0][1])

        data.update({uid: {"xp": 0, "level": 1}})

        update = "UPDATE users set data = '{0}' WHERE guild = {1}".format(json.dumps(data), guild)
        self.cursor.execute(update)
        self.db.commit()

    async def add_xp(self, user: int, guild: int, bot, mchannel):
        levels = await self.get_user(user, guild, only=False)

        levels[str(user)]['xp'] += random.randint(2, 8)
        level = levels[str(user)]['level']

        count = round((((level ** 2) + 50 + (level * 10)) * 2.5))

        if count <= levels[str(user)]['xp']:
            levels[str(user)]['level'] += 1
            channel = levels[0][2]

            if channel is None:
                channel = mchannel

            await cogs.levelup.Levelup.announce(bot, channel, user, levels[str(user)]['level'])

            levels[str(user)]['xp'] -= count

        save = "UPDATE users set data = '{0}' where guild = {1}".format(json.dumps(levels), guild)

        self.cursor.execute(save)

        self.db.commit()

    async def get_user(self, user, guild, only=True):
        req = "SELECT * FROM users WHERE guild = '{}'".format(guild)

        self.cursor.execute(req)
        data = self.cursor.fetchall()

        if data == [] or str(user) not in json.loads(data[0][1]).keys():
            await self.add_user(guild, user)
            self.cursor.execute(req)
            data = self.cursor.fetchall()

        json_data = json.loads(data[0][1])

        if only:
            return json_data[str(user)]

        return json_data

    async def get(self, guild):
        req = "SELECT * FROM users WHERE guild = {}".format(guild)

        self.cursor.execute(req)
        return self.cursor.fetchall()[0]

    async def setchannel(self, guild, channel):
        if channel is not None:
            req = "UPDATE users set channel = {0} WHERE guild = {1}".format(channel, guild)
        else:
            req = "UPDATE users set channel = NULL WHERE guild = {0}".format(guild)

        self.cursor.execute(req)
        self.db.commit()

    async def update(self, guild, val, quant, user):
        levels = await self.get_user(user, guild, only=False)
        
        levels[str(user)][val] += quant

        save = "UPDATE users set data = '{0}' where guild = {1}".format(json.dumps(levels), guild)

        self.cursor.execute(save)
        self.db.commit()

    async def delete(self, user: int, guild: int):
        req = "SELECT * FROM users WHERE guild = '{}'".format(guild)

        self.cursor.execute(req)

        data = json.loads(self.cursor.fetchall()[0][1])

        if not str(user) in data.keys():
            return False

        del data[str(user)]

        save = "UPDATE users set data = '{0}' where guild = {1}".format(json.dumps(data), guild)

        self.cursor.execute(save)
        self.db.commit()
        return True

    async def add_role(self, role, guild, level):

        req = "SELECT * FROM roles WHERE guild = '{}'".format(guild)

        self.cursor.execute(req)

        data = self.cursor.fetchall()

        if not data:
            act = "insert into roles VALUES ('{0}', '{{}}')".format(guild)
            self.cursor.execute(act)
            self.db.commit()
            self.cursor.execute(req)
            data = self.cursor.fetchall()

        roles = json.loads(data[0][1])

        roles[str(level)] = str(role)

        save = "UPDATE roles set data = '{0}' where guild = {1}".format(json.dumps(roles), guild)
        self.cursor.execute(save)
        self.db.commit()

    async def del_role(self, guild, role):
        req = "SELECT * FROM roles WHERE guild = {}".format(guild)

        self.cursor.execute(req)
        data = self.cursor.fetchall()

        if data == [] or str(role) not in json.loads(data[0][1]).values():
            return False

        data = json.loads(data[0][1])
        for key in list(data):
            if str(role) == str(data[key]):
                del data[key]

        save = "UPDATE roles set data = '{0}' where guild = {1}".format(json.dumps(data), guild)

        self.cursor.execute(save)
        self.db.commit()
        return True

    async def list_roles(self, guild):
        req = "SELECT * FROM roles WHERE guild = {}".format(guild)

        self.cursor.execute(req)
        return self.cursor.fetchall()

    async def reset(self, guild):
        req = "UPDATE users set data = '{{}}' where guild = {0}".format(guild)

        self.cursor.execute(req)

        self.db.commit()
