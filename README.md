Voice guided stretches.

Created this to help me count and track physical therapy excercises for my knee for skiing. 
Keyboard interaction is minimal, essentially starting a new type of stretch. Then, voice guides through similar activities so that one can focus on excercises, not counting, and finish quickly.

Originally, there was more keyboard confirmation required and it was just counting so an external timer was also required.

# Usage

Run program and follow prompts. 

Do stretches with clean UI:

```sh
py ./src/main.py run --stretch --clear
```

# Install

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Requirements

MacOS because using system voice commands.    
Works on MacOS 12.4 python 3.9.13

## Confirm voice works

Executing the following in a shell program should result in the sentence being spoken.

```sh
% say -v Susan "is not it nice to have a computer that will talk to you?"
```
