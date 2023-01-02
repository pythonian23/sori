import logging
import os
import queue
import threading
import time

import pydub
import pydub.playback

from sori.player import (
    RandomPlayer,
    FixedPlayer,
    FixedShufflePlayer,
    DeterministicShufflePlayer,
    PlaylistShufflePlayer,
)


def main():
    playlist: list[str] = []
    list_path = input()
    for v in os.walk(list_path):
        for song in v[2]:
            path = v[0] + "/" + song
            playlist.append(path)

    buffer = queue.Queue(4)

    def audio_thread(q: queue.Queue):
        while True:
            music = q.get()
            pydub.playback.play(music)
            time.sleep(0.5)

    audio = threading.Thread(target=audio_thread, args=(buffer,), daemon=True)
    audio.start()

    player = FixedPlayer

    for path in player(playlist):
        try:
            audio = pydub.AudioSegment.from_file(path)
        except pydub.exceptions.CouldntDecodeError:
            logging.log(logging.DEBUG, "Couldn't decode file: " + path)
        buffer.put(audio.fade_in(10000).fade_out(10000))


if __name__ == "__main__":
    main()
