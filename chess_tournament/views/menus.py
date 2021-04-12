import models.players
class HomeMenuPage: 
	
	@classmethod
	def homepage_options(self):
		print ("PAGE D'ACCUEIL")
		print ("pressez la touche correspondant à votre choix et appuyez sur 'Entrée'")
		print ("[1] Gestion des joueurs")
		print ("[2] Gestion des tournois")
		print ("[q] quitter le programme")

	@classmethod	
	def players_main_page_options(self):
		"""display the list of players"""
		print("[h] Retour à l'accueil")
		print("Choisissez le numéro du joueur à modifier")
		pass


