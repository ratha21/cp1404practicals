class Band:
    """A band with a name and a collection of musicians."""

    def __init__(self, name):
        """Initialise band with name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Tell each musician in the band to play."""
        for musician in self.musicians:
            musician.play()

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        musician_strs = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strs})"
