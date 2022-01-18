from chess_tournament.controllers.home_controller import HomePageController
from chess_tournament.models.players import Player
from chess_tournament.controllers.player_controller import PlayerController
from chess_tournament.controllers.tournament_controller import TournamentController
from chess_tournament.models.tournaments import Tournament, Round, Match
import subprocess as sp
from tinydb import TinyDB, Query

class Store:
    def __init__(self):
        self.data = {"players": [], "tournaments": []}
        self.db = TinyDB("database.json")
        self.player_table = self.db.table("players")
        self.tournaments_table = self.db.table("tournaments")

        players_dict = self.player_table.all()
        for player_dict in players_dict:
            self.data["players"].append(Player.from_dict(player_dict))

        tournaments_dict = self.tournaments_table.all()
        for tournament_dict in tournaments_dict:
            tournament = Tournament.from_dict(self, tournament_dict)
            self.data["tournaments"].append(tournament)

            rounds_dict = tournament_dict["rounds"]
            for round_dict in rounds_dict:
                round = Round.from_dict(self, round_dict)
                tournament.rounds.append(round)
                matches_dict = round_dict["matches"]

                for match_dict in matches_dict:
                    match_dict["player1"] = self.get_player(match_dict["player1"])
                    match_dict["player2"] = self.get_player(match_dict["player2"])
                    round.matches.append(Match.from_dict(self, match_dict))

    def save_player(self, player):
        player_query = Query()
        self.player_table.upsert(player.to_dict(), player_query.id == player.id)

    def save_tournament(self, tournament):
        tournament_query = Query()
        self.tournaments_table.upsert(
            tournament.to_dict(), tournament_query.name == tournament.name
        )

    def get_player(self, player_id):
        return next(p for p in self.data["players"] if str(p.id) == str(player_id))

    def get_all_players(self):
        return self.data["players"]

    def add_player(self, player):
        self.data["players"].append(player)
        self.save_player(player)

    def get_all_tournaments(self):
        return self.data["tournaments"]

    def get_tournament(self, tournament_name):
        return next(p for p in self.data["tournaments"] if p.name == tournament_name)

    def create_tournament(self, tournament):
        self.data["tournaments"].append(tournament)
        self.save_tournament(tournament)

class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "list_player": PlayerController.list_players,
        "new_player": PlayerController.create,
        "view_player": PlayerController.view,
        "delete_player": PlayerController.delete,
        "update_player": PlayerController.update,
        "view_tournament": TournamentController.view_tournament,
        "create_tournament": TournamentController.create_tournament,
        "list_tournaments": TournamentController.list_tournaments,
        "update_old_tournament": TournamentController.update_old_tournament,
        "create_first_round": TournamentController.create_first_round,
        "add_tournament_player": TournamentController.add_tournament_player,
        "create_next_round": TournamentController.create_next_round,
        "play_match": TournamentController.play_match,
        "select_tournament_player": TournamentController.select_tournament_player,
        "sort_players_ranking": TournamentController.sort_players_ranking,
        "sort_players_alphabetical": TournamentController.sort_players_alphabetical,
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = Store()

    def run(self):
        while not self.exit:
            sp.call("clear", shell=True)
            controller_method = self.routes[self.route]
            next_route, next_params = controller_method(self.store, self.route_params)
            self.route = next_route
            self.route_params = next_params

            if next_route == "quit":
                self.exit = True