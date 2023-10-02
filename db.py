"""
Users Table
user_id -primary key auto increment int
user_name varchar(25)
user_cntc_no varchar(10)

Task Table
task_id -primary key auto increment int
user_id -foriegn key
task_title -varchar(25)
task_description varchar(255)

# Field, Type, Null, Key, Default, Extra
'status', 'enum(\'Pending\',\'In Progress\',\'Completed\')', 'YES', '', 'Pending', ''

"""


"""
#I will follow this format iin every function in db.py
#If I add something apart from this i will comment it there

def function(#parameters if any):
    try:
        #Setup connection
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="to-do")
        cursor=conn.cursor()
        conn.start_transaction()
        
        #Write query
        query=""       #should be string
        parameters=()  #passing parameter should be list/tuple
        cursor.execute(query,parameters)
        db_return=cursor.fetchall() # the database will return if the data is found in tuple

        #returning the data,always check zeroth index of the list for true/false and and first index for data
        return [True,db_return[0]]  
    
    except Exception as e:
        #check for any error if occur
        conn.rollback()
        print(f"An error occured as:\n{e}")

        #return a list-> list[0]=true/false list[2]=data/(if false then error statement/code)
        return [False,e]
    
    finally:
        #finally commit changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()
"""

#Add,edit,delete/cancel,operations:pending,completed,cancel
import mysql.connector as mc 
import datetime


def add_user(user_details):
    #user_details->[0]=user_name,[1]=user_email,[2]=user_password
    try:
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="to_do")
        cursor=conn.cursor()
        conn.start_transaction()

        query="INSERT INTO users(user_name,user_email,user_password) VALUES (%s,%s,%s);"
        parameters=user_details

        cursor.execute(query,parameters)
        db_return=cursor.fetchall()

        return [True,db_return]

    except Exception as e:
        conn.rollback()
        print(f"An error occured as {e}")
        return[False,e]
    finally:
        conn.commit()
        cursor.close()
        conn.close()

#user_details=["Edward","edward@gmail.com","12345"]
#print(add_user(user_details))

def add_task(task_details):
    #task_details->[0]=user_id(foreign key),[1]=task_title,[2]=task_description,[3]=date
    try:
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="to_do")
        cursor=conn.cursor()
        conn.start_transaction()

        query="INSERT INTO tasks(user_id,task_title,task_description,due_date) VALUES (%s,%s,%s,%s);"
        parameters=task_details

        cursor.execute(query,parameters)
        db_return=cursor.fetchall()

        return [True,db_return]

    except Exception as e:
        conn.rollback()
        print(f"An error occured as {e}")
        return[False,e]
    finally:
        conn.commit()
        cursor.close()
        conn.close()
"""
#Since I am using date data type in sql therefore I cannot pass the date as string,
#so by using datetime module I converted to datetime data type
date=datetime.date(2023,11,18)
task_details=[1,"No Video Games today","Today I will NOT play Video Game",date]
add_task(task_details)
"""

def delete_task(task_details):
    #task_details=task_id
    try:
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="to_do")
        cursor=conn.cursor()
        conn.start_transaction()

        query="DELETE FROM tasks WHERE task_id=(%s);"
        parameters=[task_details]   #convert it into list/tuple

        cursor.execute(query,parameters)
        db_return=cursor.fetchall()

        return [True]

    except Exception as e:
        conn.rollback()
        print(f"An error occured as {e}")
        return[False,e]
    finally:
        conn.commit()
        cursor.close()
        conn.close()


#edit_1=task_title,task_description,due_date
#edit_2=change status

def edit_task(edit_code,task_details):
    """
    if edit_code is 1:
        it will ask for all these three details again
        task_title,task_details,task_date
    if edit_code is 2:
        it will ask to change its status 
        A status of the task can be in one of the following state only
        Pending,Completed,Cancelled
    """
    try:
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="to_do")
        cursor=conn.cursor()
        conn.start_transaction()
        if edit_code==1:
            #task_details->[0]=task_title,[1]=task_description,[2]=due_date,[3]=task_id
            query="UPDATE tasks SET task_title=(%s),task_description=(%s),due_date=(%s) WHERE task_id=(%s);"
            parameters=(task_details)
        elif edit_code==2:
            #task_details-> task_details[0]=update code,task_details[1]=task_id
            update_code,task_id=task_details[0],task_details[1]
            if update_code==1:
                query="UPDATE tasks SET status = 'Pending' WHERE task_id=(%s);"
                parameters=[task_id]
            elif update_code==2:
                query="UPDATE tasks SET status = 'In Progress' WHERE task_id=(%s);"
                parameters=[task_id]
            elif update_code==3:
                query="UPDATE tasks SET status = 'Completed' WHERE task_id=(%s);"
                parameters=[task_id]
            else:
                return [False,"Invalid update code"]
        else:
            return [False,"Invalid edit code"]

        
        cursor.execute(query,parameters)
        db_return=cursor.fetchall()

        return [True,db_return]

    except Exception as e:
        conn.rollback()
        print(f"An error occured as {e}")
        return[False,e]
    finally:
        conn.commit()
        cursor.close()
        conn.close()

#date=datetime.date(2023,10,10)
#task_details=["Gaming","I will play games all day now",date,2]
#task_details=[2,2]
#print(edit_task(2,task_details))

def show_tasks_db(user_id):
    #task_details=task_id
    try:
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="to_do")
        cursor=conn.cursor()
        conn.start_transaction()

        query="SELECT * FROM tasks WHERE user_id=(%s);"
        parameters=[user_id]

        cursor.execute(query,parameters)
        db_return=cursor.fetchall()

        return [True,db_return]

    except Exception as e:
        conn.rollback()
        print(f"An error occured as {e}")
        return[False,e]
    finally:
        conn.commit()
        cursor.close()
        conn.close()


