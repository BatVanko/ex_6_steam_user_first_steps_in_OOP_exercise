class SteamUser:
    def __init__(self, username, games: list):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        is_in_games = False
        for current_game in self.games:
            if game == current_game:
                is_in_games = True
        if is_in_games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, gam):
        is_in_games = False
        for cur_game in self.games:
            if gam == cur_game:
                is_in_games = True
        if is_in_games:
            return f"{gam} is already in your library"
        else:
            self.games.append(gam)
            return f"{self.username} bought {gam}"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"

user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())

