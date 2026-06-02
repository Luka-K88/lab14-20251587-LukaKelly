class Anime:
    def __init__(self, title, genre, status, rating):
        self.title = title
        self.genre = genre
        self.status = status
        self.rating = rating
    
    def displayInfo(self):
        print("=== Watchlist ===")
        print(f"Title: {self.title.title()}")
        print(f"Genre: {self.genre.title()}")
        print(f"Status: {self.status.title()}")
        print(f"Rating: {self.rating.title()}")

    def updateStatus(self):
        self.status = input("Enter 'Watched', 'Watching', or 'Waiting': ").lower()


anime1 = Anime("Demon Slayer", "Action", "Watching", "3/5")
anime2 = Anime("Spy x Family", "Comedy", "Completed", "3/5")
anime3 = Anime("Haikyuu", "Sports", "Waiting", "3/5")

anime_list = [anime1, anime2, anime3]

for i in anime_list:
    i.displayInfo()
    update = input("Update status?: ").lower()
    if update == "yes":
        print("Updating Status...")
        i.updateStatus()
        i.displayInfo()
    else:
        print("No status updated")