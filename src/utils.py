import os
import time


def countdown_timer(seconds=30):
    while seconds > 0:
        time.sleep(1)
        seconds -= 1


def say(message, voice="Susan"):
    # https://stackoverflow.com/questions/42150309/how-to-make-a-sound-in-osx-using-python-3
    os.system(f"say -v {voice} {message}")


if __name__ == "__main__":
    globals()[os.sys.argv[1]]()
