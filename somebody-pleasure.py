import time
import sys
from threading import Thread

def text_style(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    text_style(lyric, speed)

def sing_song():
    lyrics = [
        ("\nI hold imagination", 0.5, 0.1),
        ("Got full of love this sadness", 5.2, 0.09),
        ("I don't feel something special", 9.8, 0.1),
        ("Turn on the floor to get some special", 13.4, 0.08),
        ("\nNever thought I'm leaving me", 17.4, 0.1),
        ("Thought the truth that has been stolen", 21.5, 0.1),
        ("It was in a blink of an eye", 26.5, 0.1),
        ("Find a way how to say goodbye", 30.3, 0.1),
        ("\nI've got to take me away from all sadness", 33.9, 0.13),
        ("Stitch all my wounds, confess all the sins", 43.2, 0.09),
        ("\nAnd took all my insecure", 47.0, 0.1),
    ]

    threads = [Thread(target=sing_lyric, args=lyric) for lyric in lyrics]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

if __name__ == "__main__":
    sing_song()