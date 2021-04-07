players = [{"identifiant": 1, "Nom" : "Florian", "Prénom" : "Serge", "Age" : 45, "Classement" : 0, "Points" : 0},
	{"identifiant": 2, "Nom" : "Thomas", "Prénom" : "Serge", "Age" : 30, "Classement" : 0, "Points" : 0},
	{"identifiant": 3, "Nom" : "Duclou", "Prénom" : "John", "Age" : 60, "Classement" : 0, "Points" : 0},
	{"identifiant": 4, "Nom" : "Platon", "Prénom" : "Paul", "Age" : 45, "Classement" : 0, "Points" : 0},
	{"identifiant": 5, "Nom" : "Fifi", "Prénom" : "Nikita", "Age" : 79, "Classement" : 0, "Points" : 0},
	{"identifiant": 6, "Nom" : "Nakama", "Prénom" : "Juugo", "Age" : 56, "Classement" : 0, "Points" : 0},
	{"identifiant": 7, "Nom" : "Blu", "Prénom" : "Tito", "Age" : 78, "Classement" : 0, "Points" : 0},
	{"identifiant": 8, "Nom" : "Ibrahim", "Prénom" : "Abdel", "Age" : 52, "Classement" : 0, "Points" : 0}
]

class Player:
	def __init__(self,**players):
		for attr_name, attr_value in players.items():
			setattr(self, attr_name, attr_value)

	def pick_player_id(self, identifiant):
		returned_input = int(input("Indiquez l'identifiant du joueur pour le modifier: "))
		return returned_input

	def pick_player_attribute(self, identifiant):
		playerid = self.pick_player_id(identifiant)
		while playerid not in list(range(1,9)):
			print("Oups, cet identifiant n'est pas correct, réessayez : ")
			playerid = self.pick_player_id(identifiant)
		else:
			print(f"joueur{identifiant} a été choisi, que voulez-vous modifier ? ")
			self.player_change(identifiant)

	def player_change(self, identifiant):
		pass
		
	
class MainPlayerMenu:
	def __init__(self):
		pass
		
	def players_main_page_options(self):
		"""display the list of players"""
		print("[h] Retour à l'accueil")
		print("Choisissez le numéro du joueur à modifier")
	
	def players_main_page_(self):
		pass



player1 = Player(players)
player1.pick_player_attribute()

#I need to define and and initiate players
#also be able to modify one, so i need to pick it first and then modify it