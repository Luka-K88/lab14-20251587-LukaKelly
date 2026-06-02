class Anime:
    def __init__(self, title, genre, status):
        self.title = title
        self.genre = genre
        self.status = status
    
    def displayInfo(self):
        print("=== Watchlist ===")
        print(f"Title: {self.title.title()}")
        print(f"Genre: {self.genre.title()}")
        print(f"Status: {self.status.title()}")

    def updateStatus(self):
        self.status = input("Enter 'Watched', 'Watching', or 'Waiting': ").lower()


anime1 = Anime("Demon Slayer", "Action", "Watching")
anime2 = Anime("Spy x Family", "Comedy", "Completed")
anime3 = Anime("Haikyuu", "Sports", "Waiting")

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