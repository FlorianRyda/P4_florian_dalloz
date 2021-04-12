players_list = [{"identifiant" : 1, "nom" : "Florian", "prénom" : "Serge", "age" : 45, "classement" : 0, "points" : 0},
	{"identifiant" : 2, "nom" : "Thomas", "prénom" : "Serge", "age" : 30, "classement" : 0, "points" : 0},
	{"identifiant" : 3, "nom" : "Duclou", "prénom" : "John", "age" : 60, "classement" : 0, "points" : 0},
	{"identifiant" : 4, "nom" : "Platon", "prénom" : "Paul", "age" : 45, "classement" : 0, "points" : 0},
	{"identifiant" : 5, "nom" : "Fifi", "prénom" : "Nikita", "age" : 79, "classement" : 0, "points" : 0},
	{"identifiant" : 6, "nom" : "Nakama", "prénom" : "Juugo", "age" : 56, "classement" : 0, "points" : 0},
	{"identifiant" : 7, "nom" : "Blu", "prénom" : "Tito", "age" : 78, "classement" : 0, "points" : 0},
	{"identifiant" : 8, "nom" : "Ibrahim", "prénom" : "Abdel", "age" : 52, "classement" : 0, "points" : 0}
]




class PlayerPick:
	def __init__(self, identifiant, nom, prénom, age, classement, points):
		self.identifiant = identifiant
		self.nom = nom
		self.prénom = prénom
		self.age = age
		self.classement = classement
		self.points = points

	def display_players(identifiant, nom, prénom, age, classement, points):
		"""display all players"""
		print(f"{players_dict[1]")


	def pick_player_id(self, identifiant):
		"""request inout of user id"""
		returned_input = int(input("Indiquez l'identifiant du joueur pour le modifier: "))
		return returned_input

	def check_player_id(self, identifiant):
		"""check validity of user input"""
		playerid = self.pick_player_id(identifiant)
		while playerid not in list(range(1,9)):
			print("Oups, cet identifiant n'est pas correct, réessayez : ")
			playerid = self.pick_player_id(identifiant)
		else:
			print(f"joueur{identifiant} a été choisi, que voulez-vous modifier ? ")

	def pick_player_info(self):

		


	
class MainPlayerMenu:
	def __init__(self):
		pass
		
	def players_main_page_options(self):
		"""display the list of players"""
		print("[h] Retour à l'accueil")
		print("Choisissez le numéro du joueur à modifier")
	
	def players_main_page_(self):
		pass



#I need to define and and initiate players
#also be able to modify one, so i need to pick it first and then modify it