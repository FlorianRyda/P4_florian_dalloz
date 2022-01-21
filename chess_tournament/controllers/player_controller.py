from chess_tournament.models.players import Player, PlayerManager
from chess_tournament.views.player_view import PlayerView


class PlayerController:
    @classmethod
    def list_players(cls, store, route_params=None):

        choice, player_id = PlayerView.display_list(store.get_all_players())

        if choice == "1":
            return "view_player", player_id
        elif choice == "2":
            return "new_player", None
        elif choice == "3":
            return "delete_player", player_id
        elif choice == "4":
            return "update_player", player_id
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            return "list_player", None

    @classmethod
    def create(cls, store, route_params=None):
        """ """
        data = PlayerView.create_new_player()

        player = Player(**data)
        if player.is_valid():
            store.add_player(player)
        else:
            print("Informations du joueur non valide.")

        return "list_player", None

    @classmethod
    def delete(cls, store, route_params):
        store["players"] = [p for p in store["players"] if p.id != route_params]
        return "list_player", None

    @classmethod
    def view(cls, store, route_params):
        """
        Display one single player, the route_params correspond to the player ID
        we want to display
        """
        player = store.get_player(route_params)
        choice = PlayerView.detail_player(player)
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None

    @classmethod
    def update(cls, store, player_id):
        """
        Get the store instance on which the players are stored,
        Selects the player according to its id,
        Calls the view to collect the new ranking,
        Updates the selected players with the new ranking,
        """
        manager = PlayerManager(store)
        player = manager.get_player(player_id)

        data = PlayerView.update_player(player)

        player.update(**data)
        store.save_player(player)
        return "list_player", None
