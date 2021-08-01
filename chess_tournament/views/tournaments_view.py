

class TournamentView:

    @classmethod
    def display_list_tournaments(cls, tournaments):
        print("name\t\tplace\t\tstart\tend\trounds")
        for tournament in tournaments:
            print(f"{tournament.name}\t{tournament.place}\t{tournament.start}\t\t{tournament.end}\t{tournament.rounds}")

        print("1. Consulter Tournoi")
        print("2. Nouveau tournoi")
        print("3. modifier tournoi")
        print("4. Reprendre Tournoi")
        print("Q. Quitter programme")
        print("H. Page d'accueil")

        choice = input("Votre Choix: ")
        extra_info = None

        if choice in ("1", "3"):
            extra_info = input("Entrez le nom du tournoi:")

        return choice, extra_info

    @classmethod
    def detail_tournament(cls, tournament):
        print(f"nom: {tournament.name}")
        print(f"Lieu: {tournament.place}")
        print(f"Date debut: {tournament.start}")
        print(f"Date fin: {tournament.end}")
        #print(f"Id de Joueurs: {tournament.players_ids}")
        print(f"Controle temps: {tournament.time}")
        print(f"Description: {tournament.description}")
        print("")
        if not tournament.rounds:
            print("C. Créer premier round.")
        if len(tournament.players) < 8:
            print("a. ajouter joueurs au tournoi")
        print("Q. Quitter")
        print("H. Page d'accueil")
        print("")
        return input("Votre Choix:")

    @classmethod
    def create_tournament(cls):
        return {
            "name": input("Entrez un nom: "),
            "place": input("Entrez un lieu: "),
            "start": input("Entrez une date de début (jj/mm/dddd): "),
            "end": input("Entrez une date de fin (jj/mm/dddd): "),
            "time": input("Entrez le contrôle du temps: "),
            "description": input("Entrez une description: ")
        }

    @classmethod
    def update_old_tournament(cls,tournament):
        return {
            "name": input(f"Entrez un nom: [{tournament.name}]"),
            "place": input(f"Entrez un lieu: [{tournament.place}]"),
            "start": input(f"Entrez une date de début (jj/mm/dddd): [{tournament.start}]"),
            "end": input(f"Entrez une date de fin (jj/mm/dddd): [{tournament.end}]"),
            "rounds": input(f"Entrez le nombre de rounds: [{tournament.rounds}]"),
            "time": input(f"Entrez le contrôle du temps: [{tournament.time}]"),
            "description": input(f"Entrez une description: [{tournament.description}]")
            }

    @classmethod
    def add_player_tournament(cls):
        print("Ajout d'un joueur :")
        return{
        "id": input("Entrez un identifiant : "),
        "lastname": input("Entrez un nom de famille : "),
        "firstname": input("Entrez un prénom : "),
        "birth": input("Entrez une date de naissance : "),
        "gender": input("Entrez un genre : "),
        "ranking": input("Entrez un classement : ")
        }


    


        