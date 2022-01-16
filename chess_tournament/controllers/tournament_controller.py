from chess_tournament.models.tournaments import (
    Tournament,
    TournamentManager,
    Round,
    Match,
)
from chess_tournament.views.tournaments_view import TournamentView
from chess_tournament.controllers.player_controller import PlayerController
from chess_tournament.views.player_view import PlayerView
import datetime
from chess_tournament.models.players import Player
import ipdb


class TournamentController:
    @classmethod
    def list_tournaments(cls, store, route_params=None):
        choice, tournament_name = TournamentView.display_list_tournaments(
            store.get_all_tournaments()
        )
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

        if len(store.data["players"]) < 8:
            return "new_player", None
        player_ids = TournamentView.add_player_tournament(store.data["players"])

        for player_id in player_ids:
            player = store.get_player(player_id)
            tournament.players.append(player)

        store.create_tournament(tournament)

        return "view_tournament", tournament.name

    @classmethod
    def update_old_tournament(cls, store, tournament_name):
        print(tournament_name)

        tournament = store.get_tournament(tournament_name)
        data = TournamentView.update_old_tournament(tournament)
        tournament.update(**data)
        store.save_tournament(tournament)

        return "list_tournaments", None

    @classmethod
    def view_tournament(cls, store, route_params):
        tournament = store.get_tournament(route_params)

        choice, param = TournamentView.detail_tournament(tournament, store)
        choice = choice.lower()
        
        if choice == "q":
            return "quit", None
        elif choice == "h":
            return "homepage", None
        elif choice == "r":
            return "rounds_details", None
        elif not tournament.rounds and choice == "c":
            return "create_first_round", tournament
        elif tournament.rounds and len(tournament.rounds) < 4 and choice == "s":
            return "create_next_round", tournament
        elif len(tournament.rounds) == 4 and tournament.is_finished():
            return "view_tournament", tournament.name
        elif len(tournament.rounds) == 4 and tournament.is_finished() and choice == "u":
            return "select_tournament_player", tournament
        elif len(store.data["players"]) < 8 and choice == "a":
            return "add_tournament_player", tournament
        elif choice == "play_match":
            return "play_match", (tournament, param)
        elif choice == "4":
            return "sort_players_ranking", tournament
        elif choice == "5":
            return "sort_players_alphabetical", tournament
        else:
            return "view_tournament", tournament

    @classmethod
    def play_match(cls, store, param):
        tournament, match_index = param
        match = tournament.current_round.matches[match_index]
        result = TournamentView.play_match(match)
        if result in ["1", "2", "3"]:
            if result == "1":
                match.player_one_won()

            elif result == "2":
                match.player_two_won()

            elif result == "3":
                match.draw()
        else:
            return "view_tournament", tournament.name

        tournament.set_player_score(match.player1.id, match.points1)
        tournament.set_player_score(match.player2.id, match.points2)
        store.save_tournament(tournament)
        return "view_tournament", tournament.name

    @classmethod
    def select_tournament_player(cls, store, tournament):
        players_list = tournament.players
        player_id = TournamentView.select_tournament_player(players_list)
        player_instance = store.get_player(player_id)
        player_ranking = TournamentView.update_player_ranking(player_instance)
        tournament.update_ranking(player_id, player_ranking)
        return "view_tournament", tournament.name

    @classmethod
    def sort_players_ranking(self, store, tournament):
        tournament.players.sort(key=lambda x: int(x.ranking), reverse=True)
        return "view_tournament", tournament.name

    @classmethod
    def sort_players_alphabetical(self, store, tournament):
        tournament.players.sort(key=lambda x: x.lastname.lower())
        return "view_tournament", tournament.name

    @classmethod
    def create_first_round(cls, store, tournament):

        tournament.generate_1st_round()

        return "view_tournament", tournament.name

    @classmethod
    def create_next_round(cls, store, tournament):

        tournament.generate_next_round()

        return "view_tournament", tournament.name

    @classmethod
    def add_tournament_player(cls, store, tournament):
        player_data = TournamentView.add_player_tournament()
        player = Player(**player_data)
        tournament = tournament.players.append(player)
        return "view_tournament", tournament.name

