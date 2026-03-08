import os
from dotenv import load_dotenv
import oracledb
load_dotenv()
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
dsn=os.getenv("DB_DSN")
connection=oracledb.connect(user=user,password=password,dsn=dsn)
for i in range(1,21):
    sql="SELECT *FROM TASKS WHERE STUDENT_ID=:1"
    odf=connection.fetch_df_all(sql,parameters=[i],arraysize=100)
    print(odf.column_names())
    print(odf.num_columns())
    print(odf.num_rows())