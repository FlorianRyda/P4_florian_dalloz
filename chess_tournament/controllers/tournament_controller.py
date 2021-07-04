from chess_tournament.models.tournaments import Tournament, TournamentManager, Round, Match
from chess_tournament.views.tournaments_view import TournamentView
import datetime

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

        TournamentController.create_first_round(tournament)

        if tournament.is_valid():
            store.create_tournament(tournament)
        else:
            print("Informations du tournoi non valides.")


        return "list_tournaments", None

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

        choice = TournamentView.detail_tournament(tournament)
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "r":
            return "rounds_details", None
        elif not tournament.round and choice.lower() == "c":
            return "create_first_round", tournament
        if len(store.players) == 8:
            if choice.lower() == "a":
                return "add_tournament_player", tournament
            #create dynamic page with remaining players

    @classmethod
    def create_first_round(self, tournament):
        tournament.generate_1st_round()

        return "view_tournament", tournament.name

    def create_next_round(cls, tournament):
        second_round = Round("Round2")
        second_round.matches = tournament.generate_matches
        tournament.rounds.append(second_round)


    
