import os
import time


def countdown_timer(seconds=30):
    while seconds > 0:
        time.sleep(1)
        seconds -= 1


"""% say -v "?" | grep Premium                                                                        
Ava (Premium)       en_US    # Hello, my name is Ava. I am an American-English voice.
Karen (Premium)     en_AU    # Hello, my name is Karen. I am an Australian-English voice.
Matilda (Premium)   en_AU    # Hello, my name is Matilda. I am an Australian-English voice.
Zoe (Premium)       en_US    # Hello, my name is Zoe. I am an American-English voice.
"""


def say(message, voice="'Zoe (Premium)'"):
    # https://stackoverflow.com/questions/42150309/how-to-make-a-sound-in-osx-using-python-3
    os.system(f"say -v {voice} {message}")


if __name__ == "__main__":
    globals()[os.sys.argv[1]]()
