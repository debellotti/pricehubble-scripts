import click

from scripts.etl import create_table as create_db_table
from scripts.etl import ingest_structured_data, open_duckdb_connection

con = open_duckdb_connection("db/pricehubble.duckdb")


@click.command()
@click.option(
    "--db",
    prompt="The database you want to connect to",
    help="The database that you want to use to ingest data.",
)
def create_table(db):
    """Simple program that creates or connect to your database."""
    create_db_table(con)
    click.echo(f"Connected to {db}!")


@click.command()
@click.option(
    "--path", prompt="Raw data path",
    help="The path that leads to the data to ingest."
)
def ingest_data(path):
    """Simple program that ingest the requested data."""
    ingest_structured_data(con)
    click.echo(f"Data from {path} ingested!")
