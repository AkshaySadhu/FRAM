import pymysql
import dataSetGenerator
import trainer

def add_student():
    conn =  pymysql.connect("localhost", "root", "munna115", "attendance")

    cur = conn.cursor()

    USN = input("Enter USN: ")
    stuName = input("Enter student name: ")
    DOB = input("Enter date of birth (YYYY-MM-DD): ")
    address = input("Enter addres: ")
    phno = input("Enter Phone No. : ")
    secID = input("Enter sectionID: ")
    emailID = input("Enter email ID: ")
    query =  "INSERT INTO STUDENT VALUES ('" + USN + "', '" + stuName + "', '" + DOB + "', '" + phno + "', '" + secID + "', '" + emailID + "', '" + address + "');"
    try:
        cur.execute(query)
        conn.commit()
    except:
        print("An exception occured")
    
    dataSetGenerator.create_training_data(USN, secID)
    trainer.train()
    cur.close()
    conn.close()
add_student()

