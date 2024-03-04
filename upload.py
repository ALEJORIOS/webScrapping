import psycopg2

HOSTNAME = 'localhost'
DATABASE = 'HOMECENTER'
USERNAME = 'postgres'
PASSWORD = '1bbc1ffdcb5ed'
PORT = 5432

conn = None
cur = None
data = None

with open('data.txt', 'r') as f:
    data = eval(f.read())

print(data[0])
START = 'INSERT INTO public."PRODUCTS" (sku, name, price) VALUES '
VALUES = ['('+str(pr["sku"])+', '+str(pr["name"])+', '+str(pr["price"])+')' for pr in data]
SCRIPTS = START + ','.join(VALUES)
try:
    conn = psycopg2.connect(
        host = HOSTNAME,
        dbname = DATABASE,
        user = USERNAME,
        password = PASSWORD,
        port = PORT
    )

    cur = conn.cursor()
    cur.execute(SCRIPTS)
    conn.commit()

except Exception as error:
    print("error: "+error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()