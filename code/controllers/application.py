class ApplicationController:
	def __init__(self):
		self.controller = None

	def start(self):
		#instance du home menu pour lancer l'appli
		self.controller = HomeMenuController()
		#tant que self controller a une valeur, continue
		while self.controller:
		#l'attribut va sur la prochaine boucle appeler la classe suivante
			self.controller = self.controller()


class HomeMenuController:
	"""home menu we have designed"""
	#la méthode call permet d'éxécuter la classe direct
	def __init__():
		self.menu = Menu()
		#envoi du menu à la vue
		self.view = HomeMenuView(self.menu)

	def __call__(self):
		#construire le menu (1)
		self.menu.add("auto", "se connecter", ConnectionMenuController())
		self.menu.add("auto","commencer une partie", NewGameController())
		self.menu.add("q","quitter",EndScreenController())

		


class NewGameController:
	def __call__(self):
		pass

class OngoingGameController:
	pass

class RankingController:
	pass

class EndScreenController:
	pass

if __name__ == "__main__":
	app = ApplicationController()
