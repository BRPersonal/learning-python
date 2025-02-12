import os
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
from pandas.core.frame import DataFrame
from sqlalchemy import create_engine,text

# Load environment variables from .env file
load_dotenv()

# Database connection parameters
db_config = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE')
}

def _get_db_url() -> str :
    suffix = f"{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    if db_config["port"] == "3306":
        print("Generating connect url for MySql")
        return "mysql+pymysql://" + suffix
    else:
        raise ValueError(f"Invalid port: {db_config['port']}. Expected 3306 for MySQL or 5432 for PostgreSQL.")

def _execute_sql_query(query : str, params : dict = None) -> DataFrame:
    db_url = _get_db_url()
    engine = create_engine(db_url)

    with engine.connect() as connection:
        # Use text() to create a prepared statement
        result_set = connection.execute(text(query), params or {})
        df = pd.DataFrame(result_set.fetchall(), columns=result_set.keys())

    return df

if __name__ == "__main__":
    df = _execute_sql_query("select id,last_name from customers order by id; ")
    print(df)