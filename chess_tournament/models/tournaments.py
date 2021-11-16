import datetime
from operator import attrgetter
import ipdb


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
		self.scores = {}

	
	def set_player_score(self, player_id, points):
		self.scores[player_id] = self.scores.get(player_id, 0) + points
		


	def is_valid(self):
		return True

	def generate_1st_round(self):
	
		match_list = []
		ordered_players = sorted(self.players, key=attrgetter("ranking"))
		first_list = ordered_players[0:4]
		second_list = ordered_players[4:9]

		zipped_list = zip(first_list,second_list)
		for player1, player2 in zipped_list:
			match = Match(player1, player2)
			match_list.append(match)
		first_round = Round("Round1")
		first_round.matches = match_list

		self.rounds.append(first_round)

	def generate_next_round(self):
		#create new round instance with the right name automatically
		current_round = Round("Round"+(str(len(self.rounds)+1)))
		#sort by score and ranking 
		tournament_players = self.players
		sorted_players = tournament_players.sort(key=lambda x: (x.score, x.ranking), reverse=True)
		ipdb.set_trace()
		first_list = sorted_players[0:4]
		second_list = sorted_players[4:9]
		available_players = zip(first_list,second_list)

		while available_players:
			#extract first player
			current_player = available_players.pop(0)
			for i, available_player in enumerate(available_players):
				if not self.tournament.has_played(current_player, available_player):
					match = Match(current_player, available_player)
					current_round.matches.append(match)
					del available_players[i]
					break
				else:
					match = Match(current_player, available_players[0])
					current_round.matches.append(match)
					del available_players[0]





	def get_current_round(self):
		return self.rounds[-1]

	


	


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
		return f"{self.round_name}: {self.matches}"

	def end(self):
		self.datetime_end = datetime.datetime.now()
		

class Match:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.points1 = None
		self.points2 = None

	def __repr__(self):
		return f"{self.player1} vs {self.player2}"

	def player_one_won(self):
		self.points1 = 1
		self.points2 = 0

	def player_two_won(self):
		self.points1 = 0
		self.points2 = 1
	
	def draw(self):
		self.points1 = 0.5
		self.points2 = 0.5

	def is_finished(self):
		return self.points1 is not None and self.points2 is not None

	def has_played(self, player1, player2):
		return self.is_finished() and player1 in (self.player1, self.player2) and player2 in (self.player1, self.player2)
 
	

		

	# def __repr__(self):
	# 	return f" Joueur 1 nom/score: {self.player1}/{self.score1}, Joueur 2 nom/score: {self.player2}/{self.score2}"
		

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
