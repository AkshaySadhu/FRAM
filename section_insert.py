import pymysql


conn = pymysql.connect('localhost', 'root', 'munna115', 'attendance')
cur = conn.cursor()


def add_section():
    secID = input("Enter section ID")
    secname = input("Enter section name: ")
    query = "INSERT INTO SECTION VALUES ('" + secID + "', '" + secname + "');"
    try:
        cur.execute(query)
        conn.commit()
    except:
        print("An exception occured")


add_section()
cur.close()
conn.close()

     
     
