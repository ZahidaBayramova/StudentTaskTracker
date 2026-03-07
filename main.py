import oracledb
conn=oracledb.connect(user="SYSTEM",password="Zahide54321@",dsn="192.168.0.196/XEPDB1")
cur=conn.cursor()
cur.execute("SELECT student_id from students")
rows = cur.fetchall()
if rows:
    for  student_id in rows:
        print(f" Student ID: {student_id}")
else:
    print("Cədvəldə student yooxdur")

cur.close()
conn.close()