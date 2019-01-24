import pymysql;

con = pymysql.connect("localhost","root","nithish24","attendance")
cur = con.cursor()

def add_lecturer():
    lecturerID = input("Enter your lecturerId: ")
    lecturerName = input("Enter Name: ")
    ldob = input("Enter date of birth(YYYY-MM-DD) : ")
    lphoneNo = input("Enter phone No. : ")
    address = input("Enter address : " )
    LemailID = input("Enter  email: ")
    Password = input("Enter password: ")
    query = "INSERT INTO LECTURER VALUES ('" +lecturerID+"', '"+lecturerName+"', '"+ldob+"', '"+lphoneNo+"', '"+address+"', '"+LemailID+"', '"+Password+"');"
    try:
        cur.execute(query)
        con.commit()
    except:
        print("An exception occured")

add_lecturer()
cur.close()
con.close()
