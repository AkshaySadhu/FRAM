import pymysql;

con = pymysql.connect("localhost","root","nithish24","attendance")
cur = con.cursor()

def add_subject():
    subjectId = input("Enter the subjectID: ")
    subjectname = input("Enter the subjectname: ")
    query = "INSERT INTO SUBJECT VALUES ('" +subjectId+"', '"+subjectname+"');"
    try:
        cur.execute(query)
        con.commit()
    except:
        print("An exception occured")

add_subject()
cur.close()
con.close()

