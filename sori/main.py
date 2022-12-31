import logging
import os
import queue
import threading
import time

import pydub
import pydub.playback


def main():
    playlist: dict[str, str] = {}
    list_path = input()
    for v in os.walk(list_path):
        for song in v[2]:
            path = v[0] + "/" + song
            playlist[song] = path

    q = queue.Queue(4)

    def player_thread(q: queue.Queue):
        while True:
            song, audio = q.get()
            logging.log(logging.INFO, song)
            pydub.playback.play(audio)
            time.sleep(10)

    player = threading.Thread(target=player_thread, args=(q,), daemon=True)
    player.start()

    for song, path in playlist.items():
        audio = pydub.AudioSegment.from_file(path)
        q.put((song, audio.fade_in(10000).fade_out(10000)))


if __name__ == "__main__":
    main()
