

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import config

# conn = psycopg2.connect(
#     host=config.pg_host,
#     database=config.pg_database,
#     user=config.pg_user,
#     password=config.pg_password)

params = {
    'dbname': 'postgres',
    'user': config.pg_user,
    'password': config.pg_password,
    'host': config.pg_host
}

conn = psycopg2.connect(**params)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

new_db_name = 'AdventureWorks'
cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_db_name)))

cur.close()
conn.close()