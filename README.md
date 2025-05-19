# pricehubble-scripts

Ensure to have Docker Daemon installed and up & running in your system.

Follow the following steps:

1. Build the project docker image: `pipenv run docker build -t pricehubble_etl:latest .`
2. Run the image inside a docker container: `docker run -i -t pricehubble_etl:latest /bin/bash` 
3. Once you are into the docker container run the following bash commands:
    - `pipenv install` #ensure that dipendencies are correctly installed
    - `pipenv run python scripts/etl.py` #launch manually the etl pipeline
4. Once the scripts has finished its execution, check the final table ("properties") rows


# pipeline scheduling

The ETL is organized in two simple step:
 - the creation of properties table
 - the ingestion of data from jsonl file to the table itself, comprehensive of data transformation and filtering operations, because duckdb allow to handle them in a very efficient and straight way via sql code

 These two steps are separated in order to allow airflow to build a DAG combining these two steps together.

 In the project I've provided a very simple example to do that by building a very simple DAG.

 This part of the code is just an example to show how to do that, in a real project these kind of things need to be managed more in details, and using separated repos.

 For the sake of clarity and semplicity I've decided to maintain the code as simple as possible (realizing a quick and dirty solution) and I've provided a very quick way to execute code and see results.