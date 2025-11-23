class Band:
    def __init__(self, name):
        """Initialize the band, set the name and the list of musicians"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add musicians to the band"""
        self.musicians.append(musician)

    def __str__(self):
        """Return the string representation of the band, including the band name and all the musicians"""
        musicians_str = ", ".join(str(self.musicians) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"

    def play(self):
        """Call the play method of all musicians and output the playing status"""
        for musician in self.musicians:
            print(musician.play())

