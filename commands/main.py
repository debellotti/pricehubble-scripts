import click

from scripts.etl import ingest_structured_data


@click.command()
@click.option('--db', prompt='The database you want to connect to',
              help='The database that you want to use to ingest data.')
def create_table(db):
    """Simple program that creates or connect to your database."""
    click.echo(f"Connected to {db}!")


@click.command()
@click.option('--path', prompt='Raw data path',
              help='The path that leads to the data to ingest.')
def ingest_data(path):
    """Simple program that ingest the requested data."""
    ingest_structured_data()
    click.echo(f"Data from {path} ingested!")
