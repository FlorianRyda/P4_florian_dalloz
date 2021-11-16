
class Player:
	def __init__(self, id, lastname, firstname, birth, gender, ranking):
		self.id = id
		self.lastname = lastname
		self.firstname = firstname
		self.birth = birth
		self.gender = gender
		self.ranking = ranking

		
	def __repr__(self):
		return f"Player #{self.id} {self.firstname} {self.lastname.upper()}" 

	def update(self, id, lastname, firstname, birth, gender, ranking):
		self.id = id
		self.lastname = lastname
		self.firstname = firstname
		self.birth = birth
		self.gender = gender
		self.ranking = ranking

	def is_valid(self):
		return True
			


class PlayerManager:
	def __init__(self, store):
		self.store = store

	def get_player(self, player_id):
		return next(p for p in self.store.data["players"] if p.id == player_id)

	def get_all(self):
		return self.store["players"]

	

			
