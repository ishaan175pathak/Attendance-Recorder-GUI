from sys import api_version
import mysql.connector as dc
import datetime
import calendar

connection = dc.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "list"
)
pointer = connection.cursor()
    
ls = [] # Fetching data from DATABASE
inp = [] # Storing input from user 
final_list = [] # Storing final result

def fetching_data():
    
    pointer.execute("Select * from list")

    info = pointer.fetchall()


    for alpha in info:
        ls.append(alpha[0])


def compare(lst):

    for a in lst:
        inp.append(a)

    fetching_data()

    for alpha in ls:
        if alpha in inp:
                final_list.append("Present")
        else:
                final_list.append("Absent")
    
def save_file_present(lst):
    
    compare(lst)

    date = datetime.date.today()
    day = date.weekday()

    query = "ALTER TABLE list ADD {0} VARCHAR(100)".format(str(calendar.day_name[day]))
    pointer.execute(query)
    connection.commit()
    
    query = "UPDATE list SET {0} = (%s) WHERE roll_number = (%s)".format(str(calendar.day_name[day]))

    for alpha,beta in zip(ls,final_list):
        pointer.execute(query,(beta,alpha,))

    connection.commit()

    pointer.close()

def save_file_absent(lst):
    for a in lst:
        inp.append(a)

    fetching_data()

    for alpha in ls:
        if alpha in inp:
                final_list.append("Absent")
        else:
                final_list.append("Present")

    date = datetime.date.today()
    day = date.weekday()

    query = "ALTER TABLE list ADD {0} VARCHAR(100)".format(str(calendar.day_name[day]))
    pointer.execute(query)
    connection.commit()
    
    query = "UPDATE list SET {0} = (%s) WHERE roll_number = (%s)".format(str(calendar.day_name[day]))

    for alpha,beta in zip(ls,final_list):
        pointer.execute(query,(beta,alpha,))

    connection.commit()

    pointer.close()

# (25,'Ishaan Pathak',A,A,P,P)

def calculate_attendence(name):

    pointer.execute("SELECT * FROM list WHERE name = (%s)",(name,))
    total = pointer.fetchall()

    total_attendence = 0
    days_present = 0

    for attend in total:
        for days in attend:
            if days == "Present":
                days_present += 1
                total_attendence += 1
            elif days == "Absent":
                total_attendence += 1
    
    return ((days_present/total_attendence)*100)