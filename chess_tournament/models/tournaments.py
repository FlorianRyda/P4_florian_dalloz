from datetime import datetime
from operator import attrgetter
import ipdb


class Tournament:
    def __init__(self, name, place, time, description):
        self.name = name
        self.place = place
        self.start = datetime.now()
        self.end = None
        self.rounds = []
        self.players = []
        self.time = time
        self.description = description
        self.scores = {}

    def set_player_score(self, player_id, points):
        self.scores[player_id] = self.scores.get(player_id, 0) + points

    def update_ranking(self, player_id, ranking):
        self.players[player_id] = self.players.get(player_id, 0) + ranking

    def is_valid(self):
        return True

    def generate_1st_round(self):

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
        current_round = Round("Round" + (str(len(self.rounds) + 1)))
        self.rounds.append(current_round)
        # sort by score and ranking
        available_players = self.players.copy()
        for player in available_players:
            player.score = self.scores.get(player.id, 0)
        available_players.sort(key=lambda x: (x.score, x.ranking), reverse=True)

        while available_players:
            # extract first player
            current_player = available_players.pop(0)

            for i, available_player in enumerate(available_players):
                if not self.has_played(current_player, available_player):
                    match = Match(current_player, available_player)
                    current_round.matches.append(match)
                    del available_players[i]
                    break

    def has_played(self, player1, player2):
        for round in self.rounds:
            if round.has_played(player1, player2):
                return True
        return False

    def is_finished(self):
        return all(round.is_finished() for round in self.rounds)

    # def set_start_time(self):
    # 	self.start = datetime.date.now()

    def set_end_time(self):
        self.end = datetime.now()

    def update(self, name, place, start, end, time, description):
        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.time = time
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "place": self.place,
            "start": datetime.timestamp(self.start) if self.start else None,
            "end": datetime.timestamp(self.end) if self.end else None,
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
    def from_dict(cls, tournament_dict):
        return cls(
            tournament_dict["name"],
            tournament_dict["place"],
            tournament_dict["time"],
            tournament_dict["description"],
        )


class TournamentManager:
    def __init__(self, store):
        self.store = store

    def get_tournament(self, tournament_name):
        return next(
            p for p in self.store.data["tournaments"] if p.name == tournament_name
        )

    def get_all_tournaments(self):
        return self.store["tournaments"]


class Round:
    def __init__(
        self, round_name, datetime_start=None, datetime_end=None, matches=None
    ):
        self.round_name = round_name
        self.datetime_start = datetime_start if datetime_start else datetime.now()
        self.datetime_end = datetime_end
        self.matches = matches if matches else []

    def __repr__(self):
        return f"{self.round_name}: {self.matches}"

    def end(self):
        self.datetime_end = datetime.now()

    def has_played(self, player1, player2):
        for match in self.matches:
            if match.has_played(player1, player2):
                return True
        return False

    def is_finished(self):
        return all(match.is_finished() for match in self.matches)

    def to_dict(self):
        return {
            "round_name": self.round_name,
            "datetime_start": datetime.timestamp(self.datetime_start)
            if self.datetime_start
            else None,
            "datetime_end": datetime.timestamp(self.datetime_end)
            if self.datetime_end
            else None,
            "matches": [m.to_dict() for m in self.matches],
        }

    @classmethod
    def from_dict(cls, tournament_dict):
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
        return (
            self.is_finished()
            and player1 in (self.player1, self.player2)
            and player2 in (self.player1, self.player2)
        )

    def to_dict(self):
        return {
            "player1": self.player1.id,
            "player2": self.player2.id,
            "points1": self.points1,
            "points2": self.points2,
        }

    @classmethod
    def from_dict(cls, round_dict):
        return cls(**round_dict)
