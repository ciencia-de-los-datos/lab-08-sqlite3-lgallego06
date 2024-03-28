import sqlite3
import pandas as pd 
def load_data():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    with open("create_tables.sql", encoding="utf-8") as file:
        cur.executescript(file.read())

    return conn, cur
conn, _ = load_data()
with open("pregunta_14.sql", encoding="utf-8") as file:
        query = file.read()
print(pd.read_sql_query(query, conn).to_dict() == {
        "K0": {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"},
        "avg(c21)": {
            0: 593.495,
            1: 575.47,
            2: 530.7529999999999,
            3: 655.6125,
            4: 555.323076923077,
        },
    })
print(pd.read_sql_query(query, conn).to_dict())