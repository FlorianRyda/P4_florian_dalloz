class HomeView:

    @classmethod
    def home(cls):
        print("Bienvenu(e)\nVeuillez indiquer votre choix puis presser 'Entree'")
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois\n")
        print("Q. Exit\n")

        return input("Choice: ")
