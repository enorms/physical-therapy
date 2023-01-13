#!python3

import os
import random
from datetime import datetime
from pathlib import Path
from typing import Union
import click

import utils
import data

# https://stackoverflow.com/questions/3961581/in-python-how-to-display-current-time-in-readable-format
time_format = "%Y-%m-%d %H:%M"
# create dir if not present
output_dir = Path("./_data")
os.makedirs(output_dir, exist_ok=True)
output_file = Path("./_data/output.txt")

# Shared args
@click.group()
@click.option("--debug", "-d", is_flag=True, help="Use debug mode")
@click.option("--verbose", "-v", is_flag=True, help="Use verbose mode")
def cli(debug, verbose):
    click.echo("Debug mode is on") if debug else None
    click.echo("Verbose mode is on") if verbose else None


@cli.command()
@click.option("--clear", "-c", is_flag=True, help="Clear screen each time")
def run(clear):
    """Main program"""

    click.clear()  # start clean
    random.shuffle(data.stretches_data)
    therapies: Union[list[data.Stretch], list[data.Stretch]] = [
        data.Stretch(**datum) for datum in data.stretches_data
    ]

    # seconds
    almost_done = 5
    delay = 2

    for t in therapies:
        click.secho(t.name, bold=True)
        click.secho(
            message=f"Sets in exercise: {t.sets}",
            fg="blue",
            nl=True,
        )
        if t.hold != -1:
            click.secho(f"Hold time: {str(t.hold)} sec", fg="blue", nl=True)
        click.echo("")
        utils.say(f"Ready for {t.name}?")
        click.pause(info=click.style("Ready? Enter any key to start", fg="yellow"))
        for set_number in range(0 + 1, t.sets + 1):
            utils.say(f"Get ready for set {set_number}")
            click.secho(f"Hold time: {str(t.hold)} sec", fg="yellow", nl=True)
            for side in ["right", "left"]:
                utils.countdown_timer(delay)
                utils.say(f"Get ready for {side} side")
                utils.countdown_timer(delay)
                utils.say(f"Go")
                utils.countdown_timer(t.hold - 4)
                utils.say(f"Almost done")
                utils.countdown_timer(almost_done - 1)
                utils.say(f"Stop")
            utils.say(f"Set {set_number} done")
            click.echo(
                message="Sets complete: " + str(set_number) + " of " + str(t.sets),
                nl=True,
            )
        click.secho(f"You finished {t.name}! woot woot keep it up", fg="green")
        utils.say(f"{t.name} done")
        click.clear()
        to_write = str(t.name) + " " + datetime.now().strftime(time_format) + "\n"
        # creates file if not present
        with output_file.open("a") as f:  # can delete by hand if needed
            f.write(to_write)
    utils.countdown_timer(delay)
    utils.say(f"All done")
    click.echo("You finished all exercises!!! You are the greatest")
    click.echo("Maybe do some stretches or meditate?")


if __name__ == "__main__":
    cli()
