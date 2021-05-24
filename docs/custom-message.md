# Messages personalisés FRank
---------
### Arguments possibles des messages personalisés

Argument|Description|Exemple d'utilsation|Rendu
:---:|:------:|:---:|:---:
`id`|id de l'utilisateur|`L'utilisateur avec l'id {id} vient de changer de niveau !`|L'utilisateur avec l'id 738341837395197952 vient de changer de niveau !
`name`|nom de l'utilisateur|`{name} vient de monter d'un niveau.`| FRank vient de monter d'un niveau
`mention`|mentionne l'utilisateur|`{mention} a gagné un niveau !`|@FRank#7228 vient de gagner un niveau
`level`|niveau de l'utilisateur|`Je crois bien que quelqu'un est passé niveau {level} 👀`|Je crois bien que quelqu'un est passé niveau 69 👀
`old_level`|l'ancien niveau de l'utilisateur| `Je crois bien que quelqu'un a dépassé le niveau {old_level} 👀`|Je crois bien que quelqu'un a dépassé le niveau 57 👀
`channelName`|nom du salon (vocal ou textuel) où l'xp a été gagné|`Quelqu'un a monté d'un niveau dans le salon {channel_name} !`| Quelqu'un a monté d'un niveau dans le salon blagues-vaseues !
`channelMention`| mention du salon (vocal ou textuel)  où l'xp a été gagné|`Une personne a tellement spammé {channelMention} qu'elle a gagné un niveau`| Une personne a tellement spammé #memes qu'elle a gagné un niveau
`xp`| Xp nécéssaire pour passer au prochain niveau|`Il faudra {xp} xp à quelqu'un pour passer au prochain niveau`|Il faudra 888 xp à quelqu'un pour passer au prochain niveau

/!\ inserrer un texte entre `{}` non présent dans la liste ci-dessus entrainera une erreur. Voici comment régler ce soucis:

`Bla bla bla {bla_bla}` affichera une erreure

`Bla bla bla {{bla_bla}}` affichera "Bla bla bla {bla_bla}"

### Exemples d'utilisation

"Bravo à {mention}, tu viens de passer niveau {level} dans {channelMention}, il lui faudra {xp} pour passer au prochain niveau !"
> Bravo à @FRank#7228, tu viens de passer niveau 60 dans #blagues-tres-vaseues, il lui faudra 83 pour passer au prochain niveau !


Note: D'autres arguments pourronts faire leur apparition à tout moment !
