from chess_tournament.controllers.home_controller import HomePageController
from chess_tournament.models.players import Player
from chess_tournament.controllers.player_controller import PlayerController
import subprocess as sp
import json


class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "list_player": PlayerController.list,
        "new_player": PlayerController.create,
        "view_player": PlayerController.view,
        "delete_player": PlayerController.delete,
        "update_player": PlayerController.update,
        "list_tournaments": print("nothing yet")
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = {
            "players": [
                Player(1, "Dalloz", "Florian", "12/04/1990", "h", 0),
                Player(2, "Dumont", "Claude", "15/09/2014", "h", 0),
                Player(3, "Jung", "Karl", "05/01/1970", "h", 0)
            ]
        }

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
