

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

params = {
    'dbname': 'postgres',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost'
}

conn = psycopg2.connect(**params)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

new_db_name = 'AdventureWorks'
cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_db_name)))

cur.close()
conn.close()