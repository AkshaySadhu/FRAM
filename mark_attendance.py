import pymysql
import datetime
import os
import face_recognize
import upload_photo
def mark_attendance():
    conn = pymysql.connect('localhost', 'root', 'munna115', 'attendance')
    cur = conn.cursor()
    ids = []
    usn_no = []

    secID = input("Enter sectionID: ")
    subID = input("Enter subjectID: ")
    hour = input("Enter the hour: ")
    date = datetime.date.today()
    upload_photo.upload_photo(secID, subID, hour)

    query = "SELECT imgPath FROM CLASSPHOTO WHERE sectionID =" + secID + " AND subjectID =" + subID + " AND date_ ='" + str(date) + "' AND hour =" + hour + ";"

    cur.execute(query)
    row = cur.fetchone()
    print(row)
    ids = face_recognize.face_recognize(row[0])
    print(ids)

    #corresponding USN fetch
    for i in range(len(ids)):
        query1 = "SELECT USN FROM TRAINIMAGES WHERE label = " + str(ids[i]) + ";"
        cur.execute(query1)
        wow = cur.fetchone()
        usn_no.append(wow[0])
    print(usn_no)

    for usn in usn_no:
        print(usn)
        query2 = "INSERT INTO ATTENDANCEDETAILS VALUES('" + usn + "', '"+ secID + "', '"+ subID + "', '"+ str(date) + "', '"+ hour + "', '" + "1" + "');"
        print(query2)
        cur.execute(query2)
        conn.commit()

    cur.close()
    conn.close()
mark_attendance()    
    
    
    
    
    

