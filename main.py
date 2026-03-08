import oracledb
conn=oracledb.connect(user="SYSTEM",password="Zahide54321@",dsn="192.168.0.196/XEPDB1")
cur=conn.cursor()
cur.execute("SELECT title from tasks")
rows = cur.fetchall()
if rows:
    for  title in rows:
        print(f" TASK ID: {title}")
else:
    print("Cədvəldə title  yooxdur")

cur.close()
conn.close()