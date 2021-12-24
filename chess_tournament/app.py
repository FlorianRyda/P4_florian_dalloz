from chess_tournament.controllers.home_controller import HomePageController
from chess_tournament.models.players import Player
from chess_tournament.controllers.player_controller import PlayerController
from chess_tournament.controllers.tournament_controller import TournamentController
from chess_tournament.models.tournaments import Tournament, Round, Match
from chess_tournament.views.tournaments_view import TournamentView

import subprocess as sp
import json

from tinydb import TinyDB, Query

import ipdb

class Store:
    def __init__(self):
        self.data = {'players': [], 'tournaments': []}
        self.db = TinyDB('database.json')
        self.player_table = self.db.table('players')
        self.tournaments_table = self.db.table('tournaments')
      
        players_dict = self.player_table.all()
        for player_dict in players_dict:
            self.data['players'].append(Player.from_dict(player_dict))
   

        tournaments_dict = self.tournaments_table.all()
        for tournament_dict in tournaments_dict:
            tournament = Tournament.from_dict(tournament_dict)
            self.data['tournaments'].append(tournament)
            rounds_dict = tournament_dict["rounds"]
            for round_dict in rounds_dict:
                round = Round.from_dict(round_dict)
                tournament.rounds.append(round)
                matches_dict = round_dict['matches']
                ipdb.set_trace()
                for match_dict in matches_dict:
                    match_dict["player1"] = self.get_player(match_dict["player1"])
                    match_dict["player2"] = self.get_player(match_dict["player2"])
                    round.matches.append(Match.from_dict(match_dict))



    def save_player(self, player):
        player_query = Query()
        self.player_table.upsert(player.to_dict(), player_query.id == player.id)
    
    def save_tournament(self, tournament):
        tournament_query = Query()
        self.tournaments_table.upsert(tournament.to_dict(), tournament_query.name == tournament.name)
        
    
        

    def get_player(self, player_id):
        return next(p for p in self.data["players"] if str(p.id) == str(player_id))
        # return next(p for p in self.store.data["players"][player_id] if str(p.id) == str(player_id))

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
        "play_match": TournamentController.play_match
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

