import os
import sys
import duckdb
import pandas as pd
from queries.sql import CREATE_TABLE, INGEST_DATA, SHOW_PROPERTIES_TABLE

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def open_duckdb_connection(db):
    """Open or create (if not exists) a db"""
    return duckdb.connect(db)


def create_table(con):
    """Create an empty table with the requested structure."""

    con.execute(CREATE_TABLE)


def ingest_structured_data(con):
    """Read data from a file that contains a list of json rows"""

    con.execute(INGEST_DATA)


def check_ingested_data(con):
    """Read data from the ingested table"""

    return con.execute(SHOW_PROPERTIES_TABLE).df()


if __name__ == "__main__":

    con = open_duckdb_connection("db/pricehubble.duckdb")
    create_table(con)
    ingest_structured_data(con)

    pd.set_option("display.max_rows", None)
    print(check_ingested_data(con))
