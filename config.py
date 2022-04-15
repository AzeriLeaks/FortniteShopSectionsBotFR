'''
La section ci-dessous est vos clés et jetons de développement Twitter nécessaires pour publier sur votre twitter!
Vous devez disposer d’un compte de développement Twitter pour lequel vous pouvez postuler à https://developer.twitter.com/ 
Vous devez créer une application pour accéder à vos clés à https://developer.twitter.com/en/portal/projects-and-apps 
Quel que soit le nom que vous donnez à votre application, c’est ce qui apparaîtra comme la source de l’endroit d’où votre tweet a été publié, par exemple. Twitter pour iPhone
Vos autorisations d’applications doivent avoir Lecture + Écriture, sinon elles ne seront pas publiées!
'''
class keys:
    consumer_key = ""
    consumer_secret_key = ""
    access_token = ""
    access_token_secret = ""

'''
La section ci-dessous est destinée à la personnalisation du tweet lui-même
'''
class customisation:
    Heading: str = "Les sections du shop de #Fortnite de ce soir:" #NOTE: Ceci est le texte qui va être tweeter (modifiable)
    Footer: str = "" #NOTE: Message qui apparaitra sous le tweet! (modifiable)
    Language: str = "fr" #NOTE: Langue dans la quelle les sections sortirons, choix entre: ar / de / en / es / es-419 / fr / it / ja / ko / pl / pt-BR / ru / tr
    point: str = "- " #NOTE: Ce qui apparait à côter des section (ex: - Marvel (x1) peut être modeifier)

    Brackets: bool = True #NOTE: True, la quantité sera noté: (x1); False, la quantité sera noté: x1
    showIfOne: bool = True #NOTE: True affiche la quantité, False ne l'affiche pas
    quantitySymbol: str = "x"  #NOTE: Le symbole qui apparait au quantité de section (ex: (x1) )
    beforeOrAfter: str = "before" #NOTE: before affiche le symbole: (x1); after affiche le symbole: (1x)
'''
Si vous avez un problème contacter :
Twitter: @SwiftNite
Discord: Swift-nite#9078

Si vous avez un problème de traduction :
Twitter: Azeri_Leaks
'''
