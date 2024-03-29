class TournamentView:
    @classmethod
    def display_list_tournaments(cls, tournaments):
        print("Liste des tournois passes et en cours: ")
        print("")
        for tournament in tournaments:
            print(
                f"Nom :{tournament.name}\tLieu: {tournament.place}\tDebut: {tournament.start}\tFin: {tournament.end}"
            )
        print("")
        print("1. Consulter/reprendre Tournoi")
        print("2. Nouveau tournoi")
        print("3. Modifier tournoi")
        print("Q. Quitter le programme")
        print("H. Page d'accueil")

        choice = input("Votre Choix: ")
        extra_info = None

        if choice in ("1", "3"):
            extra_info = input("Entrez le nom du tournoi:")

        return choice, extra_info

    @classmethod
    def detail_tournament(cls, tournament, store):
        """Main view of the selected tournament
        Displays all the tournament data available
        """

        print("Details du tournoi:")
        print("")
        print(f"nom: {tournament.name}")
        print(f"Lieu: {tournament.place}")
        print(f"Date debut: {tournament.start}")
        print(f"Date fin: {tournament.end}")
        print(f"Controle temps: {tournament.time}")
        print(f"Description: {tournament.description}")
        print("")

        print("liste des joueurs du tournoi:")
        for player in tournament.players:
            print(player)
        print("")

        print("Liste des Rounds: ")

        if tournament.rounds:
            for round in tournament.rounds:
                print("")
                print(f"Nom: {round.round_name}:, Debut: {round.datetime_start}, Fin: {round.datetime_end}.")
                for match in round.matches:
                    if not match.points1 and not match.points2:
                        print(f"{match.player1} vs {match.player2} en attente de resultats")
                    else:
                        print(f"{match.player1} vs {match.player2}")
                        print(f"{match.points1} vs {match.points2}")
        if not tournament.rounds:
            print("Aucun round cree")
            print("C. Creer le premier round.")
        elif len(store.data["players"]) < 8:
            print("A. Ajouter joueur(s) au tournoi")
        elif tournament.is_finished() and len(tournament.rounds) == 4:
            print("")
            print("Le tournoi est termine !")
            print("U. Mettez a jour le classements des joueurs")
            print("")
        elif not tournament.current_round.is_finished():
            print("")
            current_round = tournament.current_round
            if current_round.matches:
                print("Etat du round en cours: ")
                for i, match in enumerate(current_round.matches):
                    if match.points1 or match.points2:
                        print(f"Match {str(i+1)} termine.")
                    else:
                        print(f"Match {str(i+1)} en attente de resultats.")
                print("")

                if not current_round.matches[0].is_finished():
                    print(f"1. Jouer le match {current_round.matches[0]}")
                if not current_round.matches[1].is_finished():
                    print(f"2. Jouer le match {current_round.matches[1]}")
                if not current_round.matches[2].is_finished():
                    print(f"3. Jouer le match {current_round.matches[2]}")
                if len(current_round.matches) > 3 and not current_round.matches[3].is_finished():
                    print(f"4. Jouer le match {current_round.matches[3]}")
                choice = input("Votre choix: ")
                return "play_match", int(choice) - 1

        elif tournament.current_round.is_finished() and len(tournament.rounds) < 4:
            print("S. Creer le round suivant.")

        print("4. Trier les joueurs par classement")
        print("5. Trier les joueurs par ordre alphabetique")
        print("H. Page d'accueil")
        print("Q. Quitter le programme")
        print("")
        return input("Tapez Votre Choix:"), None

    @classmethod
    def play_match(cls, match):
        """
        Show the two players playing in the current match
        Show options available to set the winner(s)
        Return the input
        """
        print(f"Entrez le resultat du match {match.player1} vs {match.player2}:")
        print(f"1.{match.player1} gagne.")
        print(f"2.{match.player2} gagne.")
        print("3. Egalite.")
        return input("Votre choix: ")

    @classmethod
    def select_tournament_player(cls, tournament_players):
        print("Le tournoi est termine")
        print("Veuillez mettre a jour le classement de chaque joueur")
        print("")
        for player in tournament_players:
            print(player)
        print("")
        print("Choisissez le joueur grace a son identifiant")
        return input("Votre choix: ")

    @classmethod
    def update_player_ranking(cls, player):
        print(f"{player}")
        return input("Entrez le nouveau classement du joueur: ")

    @classmethod
    def create_tournament(cls):
        return {
            "name": input("Entrez un nom: "),
            "place": input("Entrez un lieu: "),
            "time": input("Entrez le controle du temps: "),
            "description": input("Entrez une description: "),
        }

    @classmethod
    def update_old_tournament(cls, tournament):
        return {
            "name": input(f"Entrez un nom: [{tournament.name}]"),
            "place": input(f"Entrez un lieu: [{tournament.place}]"),
            "time": input(f"Entrez le controle du temps: [{tournament.time}]"),
            "description": input(f"Entrez une description: [{tournament.description}]"),
        }

    @classmethod
    def add_player_tournament(cls, players):
        for player in players:
            print(player)
        ids = []
        while len(ids) < 8:
            id = input("Selectionnez un id de joueur: ")
            if not id.isnumeric():
                print("Valeur invalide, l'id doit etre un chiffre.")
                continue
            id = int(id)

            if id not in [int(p.id) for p in players]:
                print("Joueur non trouve, veuillez reessayer.")
            elif id in ids:
                print("Joueur deja selectionne, ajoutez un autre joueur.")
            else:
                ids.append(id)

        return ids

    @classmethod
    def view_selected_match(cls, match_num, match):
        print(f"Resultat du Match n°{match_num}.")
        print(f"Entrez 1 si joueur {match.player1} gagne")
        print(f"Entrez 2 si joueur {match.player2} gagne")
        print("Entrez 3 si egalite")
        return input("Indiquez le resultat ici: ")
