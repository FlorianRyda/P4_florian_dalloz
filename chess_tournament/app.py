from chess_tournament.controllers.home_controller import HomePageController
from chess_tournament.models.players import Player
from chess_tournament.controllers.player_controller import PlayerController
from chess_tournament.controllers.tournament_controller import TournamentController
from chess_tournament.models.tournaments import Tournament, Round, Match
from chess_tournament.views.tournaments_view import TournamentView

import subprocess as sp
import json

from tinydb import TinyDB, Query


class Store:
    def __init__(self):
        self.db = TinyDB('players.json')
        self.data = self.db.all()
        # import ipdb; ipdb.set_trace()
        round1 = Round("Round1")
        round1.end()
        player1 = Player(1, "Dalloz", "Florian", "12/04/1990", "h", 100)
        player2 = Player(2, "Dumont", "Claude", "15/09/2014", "h", 50)
        player3 = Player(3, "Jung", "Kuarl", "05/01/1970", "h", 105),
        player4 = Player(4, "Lebret", "Jacques", "05/11/1987", "h", 200),
        player5 = Player(5, "Tati", "Alexandre", "08/01/1971", "h", 25),
        player6 = Player(6, "Lezehar", "Nina", "12/01/1954", "f", 45),
        player7 = Player(7, "Diallo", "Aminata", "08/08/1969", "f", 10),
        player8 = Player(8, "Carmin", "Elodie", "15/06/1999", "f",90)
        
        match = Match(player1, player2)
       
        
        self.data = {
        "players": [
         player1,
        player2,
        player3,
        player4,
        player5,
        player6,
        player7,
        player8
        ],
        "tournaments" : [
            Tournament("premier", "Champigny", "12/04/2021", 
                                "15/04/2021", [player1,player2,player3,player4,player5,player6,player7,player8], "Blitz", 
                                "tournoi test"),
                                ]
        }

        

    def get_player(self, player_id):
        return next(p for p in self.data["players"] if p.id == player_id)

    def get_all_players(self):
        return self.data["players"]

    def add_player(self, player):
        self.data["players"].append(player)

    def get_all_tournaments(self):
        return self.data["tournaments"]

    def get_tournament(self, tournament_name):
        return next(p for p in self.data["tournaments"] if p.name == tournament_name)

    def create_tournament(self, tournament):
        self.data["tournaments"].append(tournament)






class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "list_player": PlayerController.list,
        "new_player": PlayerController.create,
        "view_player": PlayerController.view,
        "delete_player": PlayerController.delete,
        "update_player": PlayerController.update,
        "view_tournament": TournamentController.detail_tournament,
        "create_tournament": TournamentController.create_tournament,
        "list_tournaments": TournamentController.list_tournaments,
        "update_old_tournament": TournamentController.update_old_tournament,
        "create_first_round": TournamentController.create_first_round,
        "view_first_round": TournamentView.test_print
        # "rounds_details": TournamentController.list_rounds
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = Store()

    def run(self):
        while not self.exit:
            # Clear the shell output
            sp.call('clear', shell=True)

            # Get the controller method that should handle our current route
            controller_method = self.routes[self.route]

            # Call the controller method, we pass the store and the route's
            # parameters.
            # Every controller should return two things:
            # - the next route to display
            # - the parameters needed for the next route
            next_route, next_params = controller_method(
                self.store, self.route_params
            )

            # set the next route and input
            self.route = next_route
            self.route_params = next_params

            # if the controller returned "quit" then we end the loop
            if next_route == "quit":
                self.exit = True
