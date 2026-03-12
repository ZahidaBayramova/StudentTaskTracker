import os
from dotenv import load_dotenv
import oracledb
load_dotenv()
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
dsn=os.getenv("DB_DSN")
connection=oracledb.connect(user=user,password=password,dsn=dsn)

move = int(input("Choose an option (1-5): "))
def choose(move):
    match move:
        case 1:
            add_task()
        case 2:
            return "View all tasks"
        case 3:
            return "Update task status"
        case 4:
            return "Delete task"
        case 5:
            return "Exit"
num_of_tasks=int(input"Enter the number of task you want add:")

def add_task():
    title=input("Please enter task title:")
    description=input("Enter description for task")

    student_id=int(input("Enter student ID:"))
    teacher_id=int(input("Enter teacher ID:"))
    cursor=connection.cursor()
    insert_query="""
INSERT INTO TASKS(title,description,student_id,teacher_id)
VALUES(:title,:description,:student_id,:teacher_id)
"""
    cursor.execute(insert_query,{
        "title":title,
        "description":description,
        "student_id":student_id,
        "teacher_id":teacher_id
    })
    connection.commit()
    print("Task added!")
for _ in range(num_of_tasks):
    add_task()
    

