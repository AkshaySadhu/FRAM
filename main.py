import pymysql

conn = pymysql.connect('localhost', 'root', 'munna115', 'attendance')

cur = conn.cursor()

loginID = input("Login ID: ")
psswd = input("Password: ")


query = "SELECT lecturerID, password FROM LECTURER;"

cur.execute(query)

print(cur)

