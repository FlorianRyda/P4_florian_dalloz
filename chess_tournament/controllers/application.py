from chess_tournament.views.menus import HomeMenuPage
from chess_tournament.models.players import PlayerPick
import sys

def launch_home_menu():
	HomeMenuPage.homepage_options()
	home_menu_choices()

def home_menu_choices():
	input_choice = input("Tapez votre choix : ")
	if input_choice == "q":
		end_program()
	elif input_choice == str(1):
		PlayerPick.display_players()
	elif input_choice == str(2):
		print("Désolé, cette partie du programme n'est pas encore prête !")
		end_program()
	else : 
		print("Choix incorrect, veuillez réessayer")
		HomeMenuPage.homepage_options()
		home_menu_choices()


def end_program():
	print("Arrêt du programme.")
	sys.exit(0)

def launch_player_list():
	pass


