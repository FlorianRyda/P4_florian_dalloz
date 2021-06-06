class Tournament:
	def __init__(self, name, place, start, end, round_num, rounds, players_ids, time, description):
		self.name = name
		self.place = place
		self.start = start
		self.end = end 
		self.round_num = round_num
		self.rounds = rounds
		self.players_ids = players_ids
		self.time = time
		self.description = description

	def __repr__(self):
		return f"Informations tournoi - nom:{self.name}, lieu: {self.place}, date de début: {self.start}"

	def is_valid(self):
		return True


class TournamentManager:
	def __init__(self, store):
		self.store = store

	def get_tournament(self, tournament_name):
		return next(p for p in self.store.data["tournaments"] if p.name == tournament_name)

	def get_all_tournaments(self):
		return self.store["tournaments"]

class round:
	def __init__(self, round_name, datetime_start, datetime_end, **matches):
		self.round_name = round_name
		self.datetime_start = datetime_start
		self.datetime_end = datetime_end
		self.matches = matches


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
