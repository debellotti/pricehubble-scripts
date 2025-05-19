CREATE_TABLE = """CREATE TABLE IF NOT EXISTS properties(
        id TEXT,
        scraping_date TEXT,
        property_type TEXT,
        municipality TEXT,
        price FLOAT,
        living_area FLOAT,
        price_per_square_meter FLOAT)"""

INGEST_DATA = """INSERT INTO properties
            SELECT id, scraping_date, property_type,
            municipality, living_area,
            CAST(replace(replace(raw_price, ' ', ''),
            '€/mo.', '') AS FLOAT) AS price,
            ROUND(price/living_area, 2) AS price_per_square_meter 
            FROM read_json('unprocessed_json_data/scraping_data.jsonl')
            WHERE price_per_square_meter BETWEEN 500 AND 15000
            AND trim(property_type) = 'apartment'
            OR trim(property_type) = 'house'
            AND scraping_date > '2020-03-05'"""