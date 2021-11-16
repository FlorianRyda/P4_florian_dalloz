# -*- coding: utf-8 -*-
import ipdb

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
    def detail_tournament(cls, tournament, store):
        print("liste des joueurs :")
        for player in store.data["players"]:
            print(player)
        print("Détails du tournoi:")
        print("")
        print(f"nom: {tournament.name}")
        print(f"Lieu: {tournament.place}")
        print(f"Date debut: {tournament.start}")
        print(f"Date fin: {tournament.end}")
        #print(f"Id de Joueurs: {tournament.players_ids}")
        print(f"Controle temps: {tournament.time}")
        print(f"Description: {tournament.description}")
        print("")
        for round in tournament.rounds:
            print(f"{round.round_name} est terminé")
        print("")
        if not tournament.rounds:
            print(u"C. Créer premier round.")
        if tournament.rounds:
            print("S. Créer round suivant.")
        if len(store.data["players"]) < 8:
            print("A. ajouter joueur(s) au tournoi")
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
    def add_player_tournament(cls, players):
        for player in players:
            print(player)
        ids = []
        while len(ids) < 8:
            id = input("Sélectionner un id de joueur: ")
            if not id.isnumeric():
                print("Valeur invalide, l'id doit être un chiffre.")
                continue
            id = int(id)
            if id not in [p.id for p in players]:
                print("Joueur non trouvé, veuillez réessayer.")
            elif id in ids:
                print("Joueur déjà sélectionné, ajoutez un autre joueur.")
            else:
                ids.append(id)

        return ids

    @classmethod
    def view_current_round(cls, current_round):
        print("Informations du round en cours: ")
        #print other round information
        for i, match in enumerate(current_round.matches):
            print("Match"+str(i+1)+". ")
            if match.points1:
                print(f"Match terminé.")
            else:
                print(f"Match à jouer.")
        print("\n'q' pour quitter")
        print("'h' pour retourner à l'écran d'accueil")
        print("'t' pour retourner au tournoi en cours")
        print("")

        print("Scores du match en cours:")
        print(f"{current_round.matches[0].player1} Point(s) {current_round.matches[0].points1}.")
        print(f"{current_round.matches[0].player2} Point(s) {current_round.matches[0].points2}.")

        print(f"{current_round.matches[1].player1} Point(s) {current_round.matches[1].points1}.")
        print(f"{current_round.matches[1].player2} Point(s) {current_round.matches[1].points2}.")

        print(f"{current_round.matches[2].player1} Point(s) {current_round.matches[2].points1}.")
        print(f"{current_round.matches[2].player2} Point(s) {current_round.matches[2].points2}.")

        print(f"{current_round.matches[3].player1} Point(s) {current_round.matches[3].points1}.")
        print(f"{current_round.matches[3].player2} Point(s) {current_round.matches[3].points2}.")
        print("\nMatchs à jouer:\n")
        if not current_round.matches[0].is_finished():
            print(f"1. Jouer le match {current_round.matches[0]}")
        if not current_round.matches[1].is_finished():
            print(f"2. Jouer le match {current_round.matches[1]}")
        if not current_round.matches[2].is_finished():
            print(f"3. Jouer le match {current_round.matches[2]}")
        if not current_round.matches[3].is_finished():
            print(f"4. Jouer le match {current_round.matches[3]}")
        # if current_round.matches[0].is_finished() and current_round.matches[1].is_finished() and current_round.matches[2].is_finished() and current_round.matches[3].is_finished():
        if all( i.is_finished() for i in current_round.matches):
            print("Round terminé, veuillez retourner au tournoi en appuyant sur 't'.")
        return input("\nchoisissez une option: ")

    @classmethod
    def view_selected_match(cls, match_num, match):
        print(f"Résultat du Match n°{match_num}.")
        print(f"Entrez 1 si joueur {match.player1} gagne")
        print(f"Entrez 2 si joueur {match.player2} gagne")
        print("Entrez 3 si égalité")
        return input("Indiquez le résultat ici: ")

        



    


        