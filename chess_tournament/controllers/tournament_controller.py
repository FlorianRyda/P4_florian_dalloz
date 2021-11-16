from chess_tournament.models.tournaments import Tournament, TournamentManager, Round, Match
from chess_tournament.views.tournaments_view import TournamentView
from chess_tournament.controllers.player_controller import PlayerController
from chess_tournament.views.player_view import PlayerView
import datetime
from chess_tournament.models.players import Player
import ipdb

class TournamentController:

    @classmethod
    def list_tournaments(cls, store, route_params=None):
        choice, tournament_name = TournamentView.display_list_tournaments(store.get_all_tournaments())
        if choice == "1":
            return "view_tournament", tournament_name
        elif choice == "2":
            return "create_tournament", None
        elif choice == "3":
            return "update_old_tournament", tournament_name
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            raise Exception("Choix invalide, veuillez réessayer")
    

    
    @classmethod
    def create_tournament(cls, store, route_params=None):
        data = TournamentView.create_tournament()
        tournament = Tournament(**data)
        player_ids = TournamentView.add_player_tournament(store.data["players"])
        for player_id in player_ids:
            player = store.get_player(player_id)
            tournament.players.append(player)

        store.create_tournament(tournament)
        
        return "create_first_round", tournament

    @classmethod
    def update_old_tournament(cls, store, tournament_name):
        print(tournament_name)

        tournament = store.get_tournament(tournament_name)
        data = TournamentView.update_old_tournament(tournament)
        Tournament.update(**data)


        return "list_tournaments", None

    @classmethod
    def detail_tournament(cls, store, route_params):
        tournament = store.get_tournament(route_params)

        choice = TournamentView.detail_tournament(tournament, store).lower()
        if choice == "q":
            return "quit", None
        elif choice == "h":
            return "homepage", None
        elif choice == "r":
            return "rounds_details", None
        elif not tournament.rounds and choice == "c":
            return "create_first_round", tournament
        elif tournament.rounds and choice == "s":
            return "create_next_round", tournament
        
        if len(store.data["players"]) < 8 and choice == "a":
            return "add_tournament_player", tournament
        

    @classmethod
    def create_first_round(cls, store, tournament):
    
        tournament.generate_1st_round()

        return "create_next_round", tournament

    @classmethod
    def create_next_round(cls, store, tournament):
    
        tournament.generate_next_round()

        return "view_current_round", tournament
        

    @classmethod
    def add_tournament_player(cls, store, tournament):
        player_data = TournamentView.add_player_tournament()
        player = Player(**player_data)
        tournament = tournament.players.append(player)
        return "view_tournament", None

    @classmethod
    def control_current_round(cls, store, tournament):
        current_round = Tournament.get_current_round(tournament)
        choice = TournamentView.view_current_round(current_round).lower()
        if choice == "q":
            return "quit", None
        elif choice == "h":
            return "homepage", None
        elif choice == "t":
            return "view_tournament", tournament.name
        
        elif choice.isnumeric() and choice in ["1","2","3","4"]:
            choice = int(choice)
            match = current_round.matches[choice-1]
            result = TournamentView.view_selected_match(choice, match)
            if result == "1":
                match.player_one_won()
               
            elif result == "2":
                match.player_two_won()
                
            elif result == "3":
                match.draw()

            tournament.set_player_score(match.player1.id, match.points1)
            tournament.set_player_score(match.player2.id, match.points2)
            #go to creation of the next round immediately
            return "view_tournament", tournament
           

    
