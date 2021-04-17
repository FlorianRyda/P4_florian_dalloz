players_list = [{"identifiant" : 1, "nom" : "Florian", "prénom" : "Serge", "age" : 45, "classement" : 0, "points" : 0},
	{"identifiant" : 2, "nom" : "Thomas", "prénom" : "Serge", "age" : 30, "classement" : 0, "points" : 0},
	{"identifiant" : 3, "nom" : "Duclou", "prénom" : "John", "age" : 60, "classement" : 0, "points" : 0},
	{"identifiant" : 4, "nom" : "Platon", "prénom" : "Paul", "age" : 45, "classement" : 0, "points" : 0},
	{"identifiant" : 5, "nom" : "Fifi", "prénom" : "Nikita", "age" : 79, "classement" : 0, "points" : 0},
	{"identifiant" : 6, "nom" : "Nakama", "prénom" : "Juugo", "age" : 56, "classement" : 0, "points" : 0},
	{"identifiant" : 7, "nom" : "Blu", "prénom" : "Tito", "age" : 78, "classement" : 0, "points" : 0},
	{"identifiant" : 8, "nom" : "Ibrahim", "prénom" : "Abdel", "age" : 52, "classement" : 0, "points" : 0}
]

class Player:
	"""instanciates each player"""
	pass

class PlayerPick:
	def __init__(self, identifiant, nom, prénom, age, classement, points):
		self.identifiant = identifiant
		self.nom = nom
		self.prénom = prénom
		self.age = age
		self.classement = classement
		self.points = points

	def display_players(self, identifiant, nom, prénom, age, classement, points):
		"""displays all players info"""

		for player_information_dict in players_list:
			print(f"{identifiant}, {nom}, {prénom}, {age}, {classement}, {points}".join(**player_information_dict))
		pick_player_id()

	def pick_player_id(self, identifiant):
		"""request input of user id"""
		returned_input = int(input("Indiquez l'identifiant du joueur pour le modifier: "))
		return returned_input

	def check_player_id(self, identifiant):
		"""check validity of user input"""
		playerid = self.pick_player_id(identifiant)
		while playerid not in list(range(1,9)):
			print("Oups, cet identifiant n'est pas correct; il doit être entre 1 et 8, réessayez : ")
			playerid = self.pick_player_id(identifiant)
		else:
			pick_player_info(identifiant)

	def pick_player_info(self, identifiant):
		print(f"joueur{identifiant} a été choisi, que voulez-vous modifier ? ")


class PlayerModification():
	pass
	