# ./src/utils.py

import os
import subprocess
import time

voices = {
    "ava": "'Ava (Premium)'",  # American
    "celine": "'Compact Voice 1'",  # Aus Siri
    "joelle": "'Joelle (Enhanced)'",  # child
    "karen": "'Karen (Premium)'",  # Australian
    "matilda": "'Matilda (Premium)'",  # Australian
    "noelle": "'Noelle (Enhanced)'",  # child
    "samantha": "'Samantha (Enhanced)'",  # child
    "zoe": "'Zoe (Premium)'",  # American, cheery
}


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


def say(message: str, voice: str = ""):
    if voice and voice not in voices.keys():
        raise ValueError

    if voice:
        subprocess.run(["say", "-v", voices.get(voice), message])

    else:
        subprocess.run(["say", message])


if __name__ == "__main__":
    globals()[os.sys.argv[1]]()
