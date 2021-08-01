class PlayerView:

    @classmethod
    def display_list(cls, players):
        print("\tID FirstName LastName Birth Gender Ranking")
        for player in players:
            print(player)

        print("1. View Player")
        print("2. New Player")
        print("3. Delete Player")
        print("4. Update Player")
        print("Q. Exit")
        print("H. Homepage")

        choice = input("Choice:")
        extra_info = None

        if choice in ("1", "3", "4"):
            extra_info = int(input("Enter Player Id:"))

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
        return {
            "id": input("Entrez un identifiant : "),
            "lastname": input("Entrez un nom de famille : "),
            "firstname": input("Entrez un prénom : "),
            "birth": input("Entrez une date de naissance : "),
            "gender": input("Entrez un genre : "),
            "ranking": input("Entrez un classement : ")
        }

    @classmethod
    def update_player(cls, player):
        return {"id": input(f"Indiquez l'identifiant [{player.id}]: "),
        "lastname": input(f"Indiquez le nom de famille [{player.firstname}]: "),
        "firstname": input(f"Indiquez le prénom [{player.lastname}]: "),
        "birth": input(f"Indiquez la date de naissance [{player.birth}]: "),
        "gender": input(f"Indiquez le sexe [{player.gender}]: "),
        "ranking": input(f"Indiquez le classement [{player.ranking}]: ")
        }

    
    

