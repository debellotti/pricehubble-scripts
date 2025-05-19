import duckdb

from queries.sql import CREATE_TABLE, INGEST_DATA

def open_duckdb_connection(db):
    """Open or create (if not exists) a db"""
    return duckdb.connect(db)
    #db/pricehubble.duckdb"


def create_table(con):
    """Create an empty table with the requested structure."""

    con.execute(
        CREATE_TABLE
    )


def ingest_structured_data(con):
    """Read data from a file that contains a list of json rows"""

    con.execute(
        INGEST_DATA
    )



create_table(con)
ingest_structured_data(con)

print(con.execute("SELECT * FROM properties").fetchall())
