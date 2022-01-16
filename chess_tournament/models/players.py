import ipdb


class Player:
    def __init__(self, id, lastname, firstname, birth, gender, ranking):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.birth = birth
        self.gender = gender
        self.ranking = ranking

    def __repr__(self):
        return (
            f"Joueur #{self.id} {self.firstname} {self.lastname.upper()} {self.ranking}"
        )

    def update(self, ranking):
        self.ranking = ranking

    def is_valid(self):
        return True

    def to_dict(self):
        return {
            "id": self.id,
            "lastname": self.lastname,
            "ranking": self.ranking,
            "firstname": self.firstname,
            "gender": self.gender,
            "birth": self.birth,
        }

    @classmethod
    def from_dict(cls, player_dict):
        return cls(**player_dict)


class PlayerManager:
    def __init__(self, store):
        self.store = store

    def get_player(self, player_id):
        return next(
            p for p in self.store.data["players"] if str(p.id) == str(player_id)
        )

    def get_all(self):
        return self.store["players"]
