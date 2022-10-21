import psycopg2
conn = psycopg2.connect(host="localhost", 
                        user="postgres", 
                        password="1", 
                        dbname="sqlda", port=5432)
with conn.cursor() as cur:
        cur.execute("SELECT * FROM customers LIMIT 5")
        records = cur.fetchall()
print(records)