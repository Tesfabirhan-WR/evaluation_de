import sqlite3
from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent / "data"

def data_loader():
    path = r"data\sales.db"
    df = []
    files = ["sales", "stores", "products"]
    for file in files:
        df.append(pd.read_excel(rf"data\{file}.xlsx"))

    return df

df_sales, df_stores, df_products = data_loader()

conn = sqlite3.connect(Path(__file__).parent / "sales.db")
try:
    df_sales.to_sql("sales", conn, if_exists="replace", index=False)
    df_products.to_sql("products", conn, if_exists="replace", index=False)
    df_stores.to_sql("stores", conn, if_exists="replace", index=False)
finally:
    conn.close()

print("Données insérées avec succès dans SQLite.")

conn = sqlite3.connect("sales.db")
print(pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn))
conn.close()