from datetime import datetime
from operator import attrgetter


class Tournament:
    def __init__(self, name, place, start, end, time, description):
        self.name = name
        self.place = place
        self.start = datetime.now().strftime("%d/%m/%y %I:%M %S %p") if not start else start
        self.end = None if not end else end
        self.rounds = []
        self.players = []
        self.time = time
        self.description = description
        self.scores = {}

    def set_player_score(self, player_id, points):
        """assigns score to a player id stored on tournament instance"""
        self.scores[player_id] = self.scores.get(player_id, 0) + points

    def update_ranking(self, player_id, ranking):
        """updates ranking of player in tournament"""
        self.players[player_id] = self.players.get(player_id, 0) + ranking

    def generate_1st_round(self):
        """creates round 1
        contains pairing algorithm"""
        match_list = []
        ordered_players = sorted(self.players, key=attrgetter("ranking"))
        first_list = ordered_players[0:4]
        second_list = ordered_players[4:9]

        zipped_list = zip(first_list, second_list)
        for player1, player2 in zipped_list:
            match = Match(player1, player2)
            match_list.append(match)
        first_round = Round("Round1")
        first_round.matches = match_list
        self.rounds.append(first_round)

    def generate_next_round(self):
        """
        creates rounds 2-4
        contains pairing algorithm
        """
        current_round = Round("Round" + (str(len(self.rounds) + 1)))
        self.rounds.append(current_round)

        available_players = self.players.copy()
        for player in available_players:
            player.score = self.scores.get(player.id, 0)
        available_players.sort(key=lambda x: (x.score, x.ranking), reverse=True)

        while available_players:
            current_player = available_players.pop(0)

            for i, available_player in enumerate(available_players):

                if not self.has_played(current_player, available_player):
                    match = Match(current_player, available_player)
                    current_round.matches.append(match)
                    del available_players[i]
                    break

    def has_played(self, player1, player2):
        """
        Lets program know if pairing has already played
        """
        for round in self.rounds:
            if round.has_played(player1, player2):
                return True
        return False

    def is_finished(self):
        """Checks if all rounds are completed"""
        self.set_end_time()
        return all(round.is_finished() for round in self.rounds)

    def set_end_time(self):
        self.end = datetime.now().strftime("%d/%m/%y %I:%M %S %p")

    def update(self, name, place, start, end, time, description):
        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.time = time
        self.description = description

    def to_dict(self):
        """
        Updates or add all tournament data in json file
        """
        return {
            "name": self.name,
            "place": self.place,
            "start": self.start,
            "end": self.end,
            "rounds": [r.to_dict() for r in self.rounds],
            "players": [player.id for player in self.players],
            "time": self.time,
            "description": self.description,
            "scores": self.scores,
        }

    @property
    def current_round(self):
        if self.rounds:
            return self.rounds[-1]

    @classmethod
    def from_dict(cls, store, tournament_dict):
        """
        Extracts selected tournament data from json file
        turns data into an instance
        """
        tournament = cls(
            name=tournament_dict["name"],
            place=tournament_dict["place"],
            start=tournament_dict["start"],
            end=tournament_dict["end"],
            time=tournament_dict["time"],
            description=tournament_dict["description"],
        )
        for player_id in tournament_dict["players"]:
            tournament.players.append(store.get_player(player_id))

        return tournament


class TournamentManager:
    def __init__(self, store):
        self.store = store

    def get_tournament(self, tournament_name):
        return next(p for p in self.store.data["tournaments"] if p.name == tournament_name)

    def get_all_tournaments(self):
        return self.store["tournaments"]


class Round:
    def __init__(self, round_name, datetime_end=None, datetime_start=None):
        self.round_name = round_name
        self.datetime_start = datetime.now().strftime("%d/%m/%y %I:%M %S %p") if not datetime_start else datetime_start
        self.datetime_end = datetime_end
        self.matches = []

    def __repr__(self):
        return f"{self.round_name}: {self.matches}"

    def end(self):
        self.datetime_end = datetime.now().strftime("%d/%m/%y %I:%M %S %p")

    def has_played(self, player1, player2):
        """
        Lets program know if pairing has already played
        """
        for match in self.matches:
            if match.has_played(player1, player2):
                return True
        return False

    def is_finished(self):
        self.end()
        return all(match.is_finished() for match in self.matches)

    def to_dict(self):
        """
        Updates or add all round data in json file
        """
        return {
            "round_name": self.round_name,
            "datetime_start": self.datetime_start,
            "datetime_end": self.datetime_end,
            "matches": [m.to_dict() for m in self.matches],
        }

    @classmethod
    def from_dict(cls, store, tournament_dict):
        """Extracts selected round data from json file
        turns data into an instance"""
        return cls(
            tournament_dict["round_name"],
            tournament_dict["datetime_start"],
            tournament_dict["datetime_end"],
        )


class Match:
    def __init__(self, player1, player2, points1=None, points2=None):
        self.player1 = player1
        self.player2 = player2
        self.points1 = points1
        self.points2 = points2

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
        """
        Lets program know if pairing has already played
        """
        return (
            self.is_finished() and player1 in (self.player1, self.player2) and player2 in (self.player1, self.player2)
        )

    def to_dict(self):
        """
        Updates or add all match data in json file
        """
        return {
            "player1": self.player1.id,
            "player2": self.player2.id,
            "points1": self.points1,
            "points2": self.points2,
        }

    @classmethod
    def from_dict(cls, store, round_dict):
        """Extracts selected match data from json file
        turns data into an instance"""
        return cls(**round_dict)
