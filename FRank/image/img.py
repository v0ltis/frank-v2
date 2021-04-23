from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class Generator:
    @staticmethod
    def card(pseudo, couleur, xp, req_xp, level, membres, pos, guild_id):
        if couleur == (0, 0, 0):
            couleur = (255, 255, 255)

        try:
            main_picture = Image.open(f"image/guilds/{guild_id}.png").convert('RGBA')
            main_picture = main_picture.resize((900, 400))

        except FileNotFoundError:
            main_picture = Image.open("image/card.png").convert('RGBA')
        profile_image = Image.open("image/avatar.png").convert('RGBA')
        profile_image = profile_image.resize((110, 110))
        offset = (75, 90)
        main_picture.paste(profile_image, offset, profile_image)

        drawing = ImageDraw.Draw(main_picture)

        # Change default font following a font file.
        font = ImageFont.truetype("image/font.ttf", 100)

        # pseudo
        drawing.text((200, 70), "{} :".format(pseudo), couleur, font=font)
        font = ImageFont.truetype("image/font.ttf", 70)
        # niveau

        drawing.text((204, 144), "Niveau {}".format(level), (231, 231, 231), font=font)
        font = ImageFont.truetype("image/font.ttf", 40)
        # affichage xp
        drawing.text((70, 250), "{}/{} xp".format(xp, req_xp), couleur, font=font)
        # classement
        drawing.text((572, 252), f"{pos}e place", (231, 231, 231), font=font)

        font = ImageFont.truetype("image/font.ttf", 30)

        # pourcentage xp
        percent = round((xp / req_xp * 100), 2)
        drawing.text((70, 290), "{}% du niveau accompli".format(percent), couleur, font=font)
        # nombre membres
        drawing.text((570, 290), "sur {} membres".format(membres), (231, 231, 231), font=font)

        # lignes :
        drawing.line([(50, 350), (850, 350)], fill=(154, 154, 154), width=9)
        drawing.line([(50, 350), (round(800 * (percent / 100)) + 50, 350)], fill=couleur, width=9)

        # level à coté des barres
        drawing.text((38, 353), str(level), couleur, font=font)
        drawing.text((850, 353), str(level + 1), couleur, font=font)

        # sauvegarde
        main_picture.save('image/level.png')

    @staticmethod
    def top(data):
        count = -1
        main_picture = Image.open("image/card.png").convert('RGBA').resize((550, 900))
        for user in data:
            count += 1
            name = user["pseudo"]
            color = user["couleur"]
            if color == (0, 0, 0):
                color = (255, 255, 255)
            percent = user["percent"]
            level = user["level"]

            drawing = ImageDraw.Draw(main_picture)
            # affiche la pp
            av = Image.open("image/{}avatar.png".format(count)).convert('RGBA')

            profile_image = av.resize((75, 75))

            offset = (20, 175 * count + 75)
            main_picture.paste(profile_image, offset, profile_image)

            # affiche la place
            font = ImageFont.truetype("image/font.ttf", 35)
            drawing.text((20, 175 * count + 25), "{})".format(count + 1), color, font=font)

            # affiche le nom
            font = ImageFont.truetype("image/font.ttf", 60)

            drawing.text((100, 175 * count + 75), name, color, font=font)

            # afficher la barre 
            drawing.line(((100, 175 * count + 145),
                          (530, 175 * count + 145)), fill=(154, 154, 154), width=9)

            drawing.line(((100, 175 * count + 145),
                          ((430 * (percent / 100) + 100), 175 * count + 145)), fill=color, width=9)

            # affiche le lvl et le prochain lvl

            font = ImageFont.truetype("image/font.ttf", 35)
            drawing.text((100, 175 * count + 155), str(level), color, font=font)

            drawing.text((520, 175 * count + 155), str(level + 1), color, font=font)

        main_picture.save('image/top.png')
