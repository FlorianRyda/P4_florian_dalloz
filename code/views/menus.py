players = [
	{"identifiant": 1, "Nom" : "Florian", "Prénom" : "Serge", "Age" : 45, "Classement" : 0, "Points" : 0},
	{"identifiant": 2, "Nom" : "Thomas", "Prénom" : "Serge", "Age" : 30, "Classement" : 0, "Points" : 0},
	{"identifiant": 3, "Nom" : "Duclou", "Prénom" : "John", "Age" : 60, "Classement" : 0, "Points" : 0},
	{"identifiant": 4, "Nom" : "Platon", "Prénom" : "Paul", "Age" : 45, "Classement" : 0, "Points" : 0},
	{"identifiant": 5, "Nom" : "Fifi", "Prénom" : "Nikita", "Age" : 79, "Classement" : 0, "Points" : 0},
	{"identifiant": 6, "Nom" : "Nakama", "Prénom" : "Juugo", "Age" : 56, "Classement" : 0, "Points" : 0},
	{"identifiant": 7, "Nom" : "Blu", "Prénom" : "Tito", "Age" : 78, "Classement" : 0, "Points" : 0},
	{"identifiant": 8, "Nom" : "Ibrahim", "Prénom" : "Abdel", "Age" : 52, "Classement" : 0, "Points" : 0}
	]
class HomeMenuPage: 
	def __init__(self):
		pass

	def homepage_options(self):
		print ("PAGE D'ACCUEIL")
		print ("pressez la touche correspondant à votre choix et appuyez sur 'Entrée'")
		print ("[1] Gestion des joueurs")
		print ("[2] Gestion des tournois")
		print ("[q] quitter le programme")

class players_main_page:
	def __init__(self):
		pass
		
	def players_main_page_options(self):
		"""display the list of players"""
		print("[h] Retour à l'accueil")
		print("Choisissez le numéro du joueur à modifier")
		pass

instance = HomeMenuPage()
print (instance.homepage_options())
