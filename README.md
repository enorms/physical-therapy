Voice guided stretches.

Created this to help me count and track physical therapy stretching for my knee for skiing. 
Keyboard interaction is minimal, essentially starting a new type of stretch. Then, voice guides through similar activities so that one can focus on stretching, not counting, and finish quickly.

Originally, there was more keyboard confirmation required and it was just counting so an external timer was also required.

# Usage

## Run program and follow prompts. 

For example, Do stretches with clean UI:

```sh
py ./src/main.py run --clear
```

## Completed items are saved

A timestamped record will be saved locally to `./_data/output.txt` and contain entries like

```
Standing ITB Stretch 2022-06-20 10:16
Gastroc Stretch on Wall 2022-06-20 10:21
```

# Install

## Setup python

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Setup stretches

Stretches can be added by following the data model in `./src/data.py` and updating the stretches variables.

[ ] TODO: separate stretches variable from data model, move from repo to local

# Requirements

MacOS because using system voice commands.    
Works on MacOS 12.4 python 3.9.13

## Confirm voice works

Executing the following in a shell program should result in the sentence being spoken.

```sh
% say -v Susan "is not it nice to have a computer that will talk to you?"
```
