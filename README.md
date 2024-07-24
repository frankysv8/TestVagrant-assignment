# Recently Played Songs

This is an in-memory store for recently played songs that can accommodate a fixed number of songs per user.

## How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run the example script:
    ```sh
    python recently_played_songs.py
    ```
4. To run the tests:
    ```sh
    python -m unittest discover
    ```

## Usage

The `RecentlyPlayedSongs` class allows you to play songs for users and retrieve the list of recently played songs.

### Methods

- `play_song(user, song)`: Records that the specified song was played by the specified user.
- `get_recently_played(user)`: Returns the list of recently played songs for the specified user.

### Example

```python
store = RecentlyPlayedSongs(capacity=3)
store.play_song("user1", "S1")
store.play_song("user1", "S2")
store.play_song("user1", "S3")
print(store.get_recently_played("user1"))  # Output: ['S1', 'S2', 'S3']
```

## Testing

Tests are written using the `unittest` module. To run the tests:

```sh
python -m unittest discover
```
