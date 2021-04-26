class PlayerView:

    @classmethod
    def display_list(cls, players):
        print("\tID\tLastName\tFirstName\tBirth\tGender\tRanking")
        for player in players:
            print(f"\t{player.id}\t{player.lastname}\t{player.firstname}\t{player.birth}\t{player.gender}\t{player.ranking}")

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
            "id": input("Enter an ID: "),
            "last name": input("Enter a last name: "),
            "first name": input("Enter a first name: "),
            "birth": input("Enter a birth date: "),
            "gender": input("Enter a gender: "),
            "ranking": input("Enter a ranking: ")
        }

    @classmethod
    def update_player(cls, player):
        return {"player_id": input(f"Indiquez l'identifiant [{player.id}]: "),
        "last_name": input(f"Indiquez le nom de famille [{player.firstname}]: "),
        "first_name": input(f"Indiquez le prénom [{player.lastname}]: "),
        "naissance": input(f"Indiquez la date de naissance [{player.birth}]: "),
        "sexe": input(f"Indiquez le sexe [{player.gender}]: "),
        "classement": input(f"Indiquez le classement [{player.ranking}]: ")
        }
