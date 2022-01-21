class PlayerView:
    @classmethod
    def display_list(cls, players):
        print("Liste des joueurs")
        print("veuillez créer au moins 8 joueurs pour lancer un tournoi")
        for player in players:
            print(player)

        print("1. Voir Joueur")
        print("2. Nouveau Joueur")
        print("3. Supprimer Joueur")
        print("4. Modifier Joueur")
        print("Q. Quitter le programme")
        print("H. Page d'Accueil")

        choice = input("Choice:")
        extra_info = None

        if choice in ("1", "3", "4"):
            extra_info = int(input("Entrez l'id du joueur:"))

        return choice, extra_info

    @classmethod
    def detail_player(cls, player):
        print(f"Id: {player.id}")
        print(f"Last Name: {player.lastname}")
        print(f"First Name: {player.firstname}")
        print(f"Birth: {player.birth}")
        print(f"Gender: {player.gender}")
        print(f"Ranking: {player.ranking}")

        print("Q. Exit")
        print("H. Homepage")
        return input("Choice:")

    @classmethod
    def create_new_player(cls):
        print("Entrez les informations du nouveau joueur")
        return {
            "id": input("Entrez un identifiant : "),
            "lastname": input("Entrez un nom de famille : "),
            "firstname": input("Entrez un prénom : "),
            "birth": input("Entrez une date de naissance : "),
            "gender": input("Entrez un genre : "),
            "ranking": input("Entrez un classement : "),
        }

    @classmethod
    def update_player(cls, player):
        print(f"Modification du joueur {player}")
        print("")
        return {
            "ranking": input(f"Indiquez le nouveau classement [{player.ranking}]: ") or player.id,
        }
