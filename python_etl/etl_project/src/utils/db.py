import psycopg2
from src.utils.helpers import get_connection_config

def get_connection(name="source_db"):
    cfg = get_connection_config(name)

    return psycopg2.connect(
        host=cfg["host"],
        port=int(cfg["port"]),
        dbname=cfg["dbname"],
        user=cfg["user"],
        password=cfg["password"],
    )
