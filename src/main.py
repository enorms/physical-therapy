# Starter program with click cli examples

import click


# Shared args
@click.group()
@click.option("--debug", "-d", is_flag=True, help="Use debug mode")
@click.option("--verbose", "-v", is_flag=True, help="Use verbose mode")
def cli(debug, verbose):
    click.echo("Debug mode is on") if debug else None
    click.echo("Verbose mode is on") if verbose else None


@cli.command()
@click.option("--items", nargs=2, type=click.Tuple([int, int]))
def sum(items):
    a, b = items
    click.echo(f"sum={a + b}")
    return a + b


if __name__ == "__main__":
    cli()
