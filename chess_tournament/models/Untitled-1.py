class Player:
    def __init__(self, id, lastname, ranking):
        self.id = id
        self.lastname = lastname
        self.ranking = ranking


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.points1 = None
        self.points2 = None

    def __repr__(self):
        return f"{self.player1} vs {self.player2}"

    def player_one_won(self):
        self.points1 = 1
        self.points2 = 0

    def player_two_won(self):
        self.points1 = 0
        self.points2 = 1

    def draw(self):
        self.points1 = 0.5
        self.points2 = 0.5

    def is_finished(self):
        return self.points1 is not None and self.points2 is not None

    def has_played(self, player1, player2):
        return (
            self.is_finished()
            and player1 in (self.player1, self.player2)
            and player2 in (self.player1, self.player2)
        )


player1 = Player(1, "dalloz", 5)
player2 = Player(3, "Dio", 6)
match1 = Match(player1, player2)
match1.draw()
print(match1.has_played(player1, player2))
