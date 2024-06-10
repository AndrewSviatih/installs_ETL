import pandas as pd
from sqlalchemy import create_engine

def connect_to_db(username: str, password: str, db_name: str):
    user = username
    password = password
    host = 'localhost'
    port = '5432'
    database = db_name

    connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'

    return create_engine(connection_string)