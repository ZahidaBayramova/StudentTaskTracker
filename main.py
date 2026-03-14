import os
from dotenv import load_dotenv
import oracledb
from datetime import datetime
load_dotenv()
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
dsn=os.getenv("DB_DSN")
connection=oracledb.connect(user=user,password=password,dsn=dsn)
def add_task():
    title=input("Please enter task title:")
    description=input("Enter description for task")
    status=input("Enter status(Press enter for Pending):)")or "Pending"
    student_id=int(input("Enter student ID:"))
    teacher_id=int(input("Enter teacher ID:"))
    start_date_str=input("Enter start date(YYYY-MM-DD):")
    end_date_str=input("Enter end date(YYYY-MM-DD):")
    #Convert string input to datetime.date objects
    start_date=datetime.strptime(start_date_str,"%Y-%m-%d").date()
    end_date=datetime.strptime(end_date_str,"%Y-%m-%d").date()
    # Create a cursor and insert the new task into the database
    cursor=connection.cursor()
    insert_query="""
INSERT INTO TASKS(title,description,status,student_id,teacher_id,start_date,end_date)
VALUES(:title,:description,:status,:student_id,:teacher_id,:start_date,:end_date)
"""
    cursor.execute(insert_query,{
        "title":title,
        "description":description,
        "status":status,
        "student_id":student_id,
        "teacher_id":teacher_id,
        "start_date":start_date,
        "end_date":end_date
    })
    connection.commit()
    # Print confirmation that the task was added

    print("Task added!")
def choose(move):
    match move:
        case 1:
            num_of_tasks = int(input("Enter the number of tasks you want to add: "))
            for _ in range(num_of_tasks):
                add_task()
        case 2:
            return "View all tasks"
        case 3:
            return "Update task status"
        case 4:
            return "Delete task"
        case 5:

            print( "Exit")
            return False
while True:
    print("\n------ Student Task Tracker ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")
    move = int(input("Choose an option (1-5): "))
    if choose(move) == False:
      break



        

    

