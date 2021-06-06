from chess_tournament.models.tournaments import Tournament, TournamentManager
from chess_tournament.views.tournaments_view import TournamentView

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
        elif choice.lower == "r":
            return "rounds_details", None


    def rounds_details(self):
        pass  
