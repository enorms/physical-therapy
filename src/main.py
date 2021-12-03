#!python3
# Exercise tracker to use with
# https://kaiserpermanente.medbridgego.com/

from datetime import datetime
from pathlib import Path
from os import system
from typing import Union
import click

from data import exercises, stretches, test_exercises, Stretch, Exercise

# https://stackoverflow.com/questions/3961581/in-python-how-to-display-current-time-in-readable-format
time_format = "%Y-%m-%d %H:%M"
# will create file; requires dir
output = Path("./_data/output.txt")

# Shared args
@click.group()
@click.option("--debug", "-d", is_flag=True, help="Use debug mode")
@click.option("--verbose", "-v", is_flag=True, help="Use verbose mode")
def cli(debug, verbose):
    click.echo("Debug mode is on") if debug else None
    click.echo("Verbose mode is on") if verbose else None


@cli.command()
@click.option("--debug", "-d", is_flag=True, help="Use debug mode")
@click.option("--test", "-d", is_flag=True, help="Test")
@click.option("--stretch", "-s", is_flag=True, help="Stretches")
@click.option("--reps", "-r", is_flag=True, help="Track each rep")
@click.option("--clear", "-c", is_flag=True, help="Clear screen each time")
def exercise(clear, stretch, reps, debug, test):
    """Tracks start and completion of exercises.
    Optionally, do stretching with '-s'."""

    # call with one line
    def clear_terminal():
        if clear:
            system("clear")

    clear_terminal()  # start clean

    therapies: Union[list[Exercise], list[Stretch]] = []
    therapies = exercises
    if stretch:
        therapies = stretches
    if test:
        therapies = test_exercises

    for t in therapies:
        click.echo("\nExercise: " + t.name)
        click.echo("Sets in exercise: " + str(t.sets) + ", Reps in set: " + str(t.reps))
        if t.hold != -1:
            click.echo("Hold time: " + str(t.hold) + " sec")
        for set_ in range(0, t.sets):
            click.echo(" - Sets complete: " + str(set_) + " of " + str(t.sets))
            if click.confirm(
                " - Start set " + str(set_ + 1) + "?", default=True
            ):  # TODO, just record finish, not start
                if reps:
                    for rep in range(0, t.reps):
                        click.echo(
                            " -- Reps complete: " + str(rep) + " of " + str(t.reps)
                        )
                        if click.confirm(
                            " -- Start rep " + str(rep + 1) + "?", default=True
                        ):
                            click.echo(" -- You can do it!")
                        if click.confirm(" -- Completed rep?", default=True):
                            click.echo(" -- You did the rep!")
                if not reps:
                    click.confirm(" - Completed set?", default=True)
                click.echo(" - You completed a set! Good job you nailed it")
        click.echo("You finished an exercise! woot woot keep it up")
        clear_terminal()
        to_write = str(t.name) + " " + datetime.now().strftime(time_format) + "\n"
        with output.open("a") as f:  # can delete by hand if needed
            f.write(to_write)
    click.echo("You finished all exercises!!! You are the greatest")
    click.echo("Maybe do some stretches or meditate?")


if __name__ == "__main__":
    cli()

# TODO: track color band
# TODO: ask "what should I do today?" and check based on last time, and times per week
