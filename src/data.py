from typing import List, Optional
from pydantic import BaseModel, ValidationError


class Stretch(BaseModel):
    name: str
    sets: int
    hold: int  # seconds


# * 2 for right, left
stretches_data = [
    {
        "name": "Shins",
        "sets": 1,
        "hold": 40,
    },
    {
        "name": "Supine Gluteus Stretch",
        "sets": 2,
        "hold": 40,
    },
    {
        "name": "Quadruped Piriformis Stretch",
        "sets": 2,
        "hold": 50,
    },
    {
        "name": "Quadriceps Stretch with Chair",
        "sets": 2,
        "hold": 40,
    },
    {
        "name": "Standing ITB Stretch",
        "sets": 2,
        "hold": 20,
    },
    {
        "name": "Gastroc Stretch on Wall",
        "sets": 2,
        "hold": 30,
    },
    {
        "name": "Seated Hamstring Stretch",
        "sets": 2,
        "hold": 40,
    },
    {
        "name": "Standing Hamstring Stretch",
        "sets": 1,
        "hold": 60,
    },
    {
        "name": "Arms over head",
        "sets": 1,
        "hold": 20,
    },
    {
        "name": "Arms across",
        "sets": 1,
        "hold": 20,
    },
    {
        "name": "Chest opening",
        "sets": 1,
        "hold": 20,
    },
    {
        "name": "Back of neck",
        "sets": 1,
        "hold": 20,
    },
]


def test_stretches():
    stretches = []
    try:
        stretches = [Stretch(**datum) for datum in stretches_data]
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    test_stretches()
