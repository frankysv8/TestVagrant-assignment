import unittest
from recently_played_songs import RecentlyPlayedSongs

class TestRecentlyPlayedSongs(unittest.TestCase):
    def test_play_song(self):
        store = RecentlyPlayedSongs(capacity=3)
        store.play_song("user1", "S1")
        store.play_song("user1", "S2")
        store.play_song("user1", "S3")
        self.assertEqual(store.get_recently_played("user1"), ["S1", "S2", "S3"])

        store.play_song("user1", "S4")
        self.assertEqual(store.get_recently_played("user1"), ["S2", "S3", "S4"])

        store.play_song("user1", "S2")
        self.assertEqual(store.get_recently_played("user1"), ["S3", "S4", "S2"])

        store.play_song("user1", "S1")
        self.assertEqual(store.get_recently_played("user1"), ["S4", "S2", "S1"])

    def test_get_recently_played_empty(self):
        store = RecentlyPlayedSongs(capacity=3)
        self.assertEqual(store.get_recently_played("user2"), [])

if __name__ == "__main__":
    unittest.main()
