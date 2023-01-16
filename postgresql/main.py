import psycopg2
import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)

conn = psycopg2.connect(
    database="product",
    host="localhost",
    port="10101",
    user="postgres",
    password="postgres123"
)

cursor = conn.cursor()
#tic = time.perf_counter()
cursor.execute("""
               SELECT * FROM product""")
rows = cursor.fetchall()
#toc = time.perf_counter()

#print(f"query in {toc - tic:0.4f} seconds")
print("rows:", len(rows))
for row in rows:
    r.set(str(row[0]), str(row))

conn.close()
