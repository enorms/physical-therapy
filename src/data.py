from typing import List, Optional
from pydantic import BaseModel, ValidationError


class Excercise(BaseModel):
    name: str
    description: Optional[str] = None
    times_per_day: int
    times_per_week: int
    sets: int
    reps: int


class Stretch(BaseModel):
    name: str
    description: Optional[str] = None
    times_per_day: int
    times_per_week: int
    sets: int
    reps: int = 1  # fits in Excercise system
    hold: int  # seconds


excercise_data = [
    {
        "name": "Clamshell with Resistance",
        "times_per_day": 1,
        "times_per_week": 3,
        "sets": 3,
        "reps": 10,
    },
    {
        "name": "Bridge with Hip Abduction",
        "times_per_day": 1,
        "times_per_week": 3,
        "sets": 3,
        "reps": 10,
    },
    {
        "name": "Squat with Chair Touch and Resistance Loop",
        "times_per_day": 1,
        "times_per_week": 3,
        "sets": 3,
        "reps": 10,
    },
    {
        "name": "Sidestepping Crab Walk with Resistance Band",
        "desc": '"sets" are "laps", "reps" are "feet in hallway"',
        "times_per_day": 1,
        "times_per_week": 3,
        "sets": 3,
        "reps": 25,
    },
    {
        "name": "Standing Hip Extension with Resistance at Ankles and Counter Support",
        "times_per_day": 1,
        "times_per_week": 3,
        "sets": 3,
        "reps": 10,
    },
    {
        "name": "Standing Hip Abduction with Resistance at Ankles and Counter Support",
        "times_per_day": 1,
        "times_per_week": 3,
        "sets": 3,
        "reps": 10,
    },
]

excercises = []
try:
    excercises = [Excercise(**datum) for datum in excercise_data]
except ValidationError as e:
    print(e)


stretches_data = [
    {
        "name": "Supine Gluteus Stretch",
        "times_per_day": 1,
        "times_per_week": 7,
        "sets": 3,
        "hold": 30,
    },
    {
        "name": "Quadruped Piriformis Stretch",
        "times_per_day": 1,
        "times_per_week": 7,
        "sets": 3,
        "hold": 30,
    },
    {
        "name": "Quadriceps Stretch with Chair",
        "times_per_day": 1,
        "times_per_week": 7,
        "sets": 3,
        "hold": 30,
    },
    {
        "name": "Prone Quadriceps Stretch",
        "times_per_day": 1,
        "times_per_week": 7,
        "sets": 3,
        "hold": 30,
    },
    {
        "name": "Seated Hamstring Stretch",
        "times_per_day": 1,
        "times_per_week": 7,
        "sets": 3,
        "hold": 30,
    },
    {
        "name": "Standing ITB Stretch",
        "times_per_day": 1,
        "times_per_week": 7,
        "sets": 3,
        "hold": 30,
    },
    {
        "name": "Gastroc Stretch on Wall",
        "times_per_day": 1,
        "times_per_week": 7,
        "sets": 3,
        "hold": 30,
    },
]

stretches = []
try:
    stretches = [Stretch(**datum) for datum in stretches_data]
except ValidationError as e:
    print(e)


test_excercise_data = [
    {
        "name": "TEST - Clamshell with Resistance",
        "times_per_day": 1,
        "times_per_week": 3,
        "sets": 2,
        "reps": 2,
    },
    {
        "name": "TEST - Lift something heavy",
        "times_per_day": 1,
        "times_per_week": 3,
        "sets": 2,
        "reps": 2,
    },
]
test_excercises = [Excercise(**datum) for datum in test_excercise_data]
