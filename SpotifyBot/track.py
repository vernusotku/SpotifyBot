class Track:
    def __init__(self, id, name, artists,playlist_id = None):
        self.id = id
        self.name = name
        self.artists = artists
        self.playlist_id = playlist_id
    def __eq__(self, other):
        return self.id == other.id