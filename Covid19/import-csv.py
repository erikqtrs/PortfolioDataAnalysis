import pandas as pd
from sqlalchemy import create_engine
path = input('Ingresa el path del archivo csv: ')
user = input('Enter the user database: ')
password = input('Enter database password: ')
port = input('Enter the port of postgresql: ')
host = input('Enter the database host: ')
database = input('Enter the database name: ')
table_name = input('Table Name: ')

df = pd.read_csv(path)
df.columns = [c.lower() for c in df.columns]

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

df.to_sql(table_name, engine)