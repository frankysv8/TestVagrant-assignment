from collections import deque

class RecentlyPlayedSongs:
    def __init__(self, capacity):
        self.capacity = capacity
        self.user_songs = {}

    def play_song(self, user, song):
        if user not in self.user_songs:
            self.user_songs[user] = deque(maxlen=self.capacity)
        else:
            if song in self.user_songs[user]:
                self.user_songs[user].remove(song)
        self.user_songs[user].append(song)

    def get_recently_played(self, user):
        if user in self.user_songs:
            return list(self.user_songs[user])
        else:
            return []

# Example Usage
if __name__ == "__main__":
    store = RecentlyPlayedSongs(capacity=3)
    store.play_song("user1", "S1")
    store.play_song("user1", "S2")
    store.play_song("user1", "S3")
    print(store.get_recently_played("user1"))  # Output: ['S1', 'S2', 'S3']

    store.play_song("user1", "S4")
    print(store.get_recently_played("user1"))  # Output: ['S2', 'S3', 'S4']

    store.play_song("user1", "S2")
    print(store.get_recently_played("user1"))  # Output: ['S3', 'S4', 'S2']

    store.play_song("user1", "S1")
    print(store.get_recently_played("user1"))  # Output: ['S4', 'S2', 'S1']
