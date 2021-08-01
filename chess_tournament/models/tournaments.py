import datetime
from operator import attrgetter


class Tournament:
	def __init__(self, name, place, start, end, time, description):
		self.name = name
		self.place = place
		self.start = start
		self.end = end
		self.rounds = []
		self.players = []
		self.time = time
		self.description = description


	def is_valid(self):
		return True

	def generate_1st_round(self):
	
		first_round = Round("Round1")
        #generate matches
		#matching algorithm
		#create 4 instances of Match
		ordered_players = sorted(self.players, key=attrgetter("ranking"))
		first_list = ordered_players[0:3]
		second_list = ordered_players[4:8]
		print(first_list)
		print(second_list)
			
		tournament.rounds.append(first_round)
		return "view_first_round"
	




class TournamentManager:
	def __init__(self, store):
		self.store = store

	def get_tournament(self, tournament_name):
		return next(p for p in self.store.data["tournaments"] if p.name == tournament_name)

	def get_all_tournaments(self):
		return self.store["tournaments"]

class Round:
	def __init__(self, round_name):
		self.round_name = round_name
		self.datetime_start = datetime.datetime.now()
		self.datetime_end = None
		self.matches = []

	def __repr__(self):
		return f"{self.round_name}"

	def end(self):
		self.datetime_end = datetime.datetime.now()

class Match:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.score1 = None
		self.score2 = None


		

# TOURS/MATCHS
# Chaque tour est une liste de matchs. Chaque match consiste en une paire de joueurs 
# avec un champ de résultats pour chaque joueur. 
# Lorsqu'un tour est terminé, le gestionnaire du tournoi saisit les résultats de chaque match 
# avant de générer les paires suivantes. 
# Le gagnant reçoit 1 point, le perdant 0 point. 
# Si un match se termine par un match nul, chaque joueur reçoit 1/2 point.

# Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, 
# chacune contenant deux éléments : une référence à une instance de joueur et un score. 
# Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour. 

# En plus de la liste des correspondances, 
# chaque instance du tour doit contenir un champ de nom. 
# Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. 
# Elle doit également contenir un champ Date et heure de début et un champ Date et heure de fin, 
# qui doivent tous deux être automatiquement remplis lorsque l'utilisateur crée un tour 
# et le marque comme terminé. 
# Les instances de round doivent être stockées dans une liste 
# sur l'instance de tournoi à laquelle elles appartiennent.
