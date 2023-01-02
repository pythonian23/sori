import copy
import random


class Player:
    """
    Player determines the order of playing.
    """

    playlist: list[str]

    def __init__(self, songs: list[str]):
        self.playlist = copy.deepcopy(songs)

    def __iter__(self) -> str:
        raise NotImplementedError("Use a sublcass of Player.")


class RandomPlayer(Player):
    """
    RandomPlayer randomly selects songs with no consideration of past selections.
    """

    def __iter__(self) -> str:
        while True:
            yield random.choice(self.playlist)


class FixedPlayer(Player):
    """
    FixedPlayer plays songs in a specific order.
    """

    def __init__(self, songs: list[str]):
        super().__init__(songs)

    def __iter__(self) -> str:
        while True:
            for song in self.playlist:
                yield song


class FixedShufflePlayer(FixedPlayer):
    """
    FixedShufflePlayer shuffles the playlist once and loops it.
    """

    def __init__(self, songs: list[str]):
        super().__init__(songs)
        random.shuffle(self.playlist)


class DeterministicShufflePlayer(FixedPlayer):
    """
    DeterministicShufflePlayer works like FixedShufflePlayer,
    but changes the order of the playlist in the same way every time.
    """

    def __init__(self, songs: list[str]):
        super().__init__(songs)
        generator = random.Random()
        generator.seed(len(songs))
        generator.shuffle(self.playlist)


class PlaylistShufflePlayer(Player):
    """
    PlaylistShufflePlayer shuffles the whole playlist each time every song in the playlists has been played.
    """

    def __init__(self, songs: list[str]):
        super().__init__(songs)

    def __iter__(self) -> str:
        while True:
            random.shuffle(self.playlist)
            for song in self.playlist:
                yield song
