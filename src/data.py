from typing import List, Optional
from pydantic import BaseModel, ValidationError


class Stretch(BaseModel):
    name: str
    sets: int
    hold: int  # seconds


stretches_data = [
    {
        "name": "Supine Gluteus Stretch",
        "sets": 3,
        "hold": 30,
    },
    {
        "name": "Quadruped Piriformis Stretch",
        "sets": 3,
        "hold": 30,
    },
    {
        "name": "Quadriceps Stretch with Chair",
        "sets": 3,
        "hold": 30,
    },
    {
        "name": "Seated Hamstring Stretch",
        "sets": 3,
        "hold": 30,
    },
    {
        "name": "Standing ITB Stretch",
        "sets": 3,
        "hold": 30,
    },
    {
        "name": "Gastroc Stretch on Wall",
        "sets": 3,
        "hold": 30,
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
