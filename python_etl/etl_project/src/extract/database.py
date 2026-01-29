import pandas as pd
from src.utils.db import get_connection

def extract_sales(process_date):
    query = """
        SELECT sale_id, product_id, quantity, price, sale_date
        FROM store_analytics.sales
        WHERE sale_date <= %s
    """

    with get_connection("source_db") as conn:
        return pd.read_sql(query, conn, params=[process_date])
