#!/usr/bin/env python3

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

# fix output file saving relative to where terminal is invoked
script_path = Path(__file__).resolve()
project_root = script_path.parent
while not (project_root / "README.md").exists():
    project_root = project_root.parent
# Ensure we didn't reach the filesystem root without finding the project root
if project_root == project_root.parent:
    raise ValueError("Could not determine project root")
output_dir = project_root / "_data"
output_file = output_dir / "output.txt"
output_dir.mkdir(parents=True, exist_ok=True)


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

    almost_done = 5  # seconds
    delay = 2  # seconds

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
            utils.say(f"Get ready for set {set_number} of {t.sets}")
            click.secho(f"Hold time: {str(t.hold)} sec", fg="yellow", nl=True)
            for side in ["right", "left"]:
                utils.countdown_timer(delay)
                utils.say(f"Get ready for {side} side")
                utils.countdown_timer(delay)
                utils.say(f"Go for {t.hold} seconds")
                utils.countdown_timer(t.hold / 2)
                utils.say(f"Half way")
                utils.countdown_timer(t.hold / 2 - 2)
                utils.say(f"Ok, stop.")
            utils.say(f"Set {set_number} done")
            click.echo(
                message="Sets complete: " + str(set_number) + " of " + str(t.sets),
                nl=True,
            )
        click.secho(f"You finished {t.name}! woot woot keep it up", fg="green")
        utils.say(f"{t.name} done")
        click.clear()
        to_write = str(t.name) + ", " + datetime.now().strftime(time_format) + "\n"
        with output_file.open("a") as f:
            f.write(to_write)
    utils.countdown_timer(delay)

    final_msg = "All done."
    final_encouragement = (
        "You finished all your exercises!!! You are the greatest. Have a wonderful day!"
    )
    utils.say(final_msg)
    utils.say(final_encouragement)
    click.echo(final_msg)
    click.echo(final_encouragement)


if __name__ == "__main__":
    cli()
