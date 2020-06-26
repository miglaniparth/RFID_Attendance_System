import mysql.connector

# We assume that the card numbers are stored in log.txt file
# For the sake of submitting the screenshots and for better understanding we have assumed SAP ID as card number
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dell@1234",
    auth_plugin='mysql_native_password',
    database='attendance'
)
mycursor = mydb.cursor()
f = open("log.txt", "r")
lines = f.readlines()
for line in lines:
    card = "{}".format(line.strip())
    sql = f"UPDATE student_attendance SET attendance = 'P' WHERE card_number = '{card}'"
    print(sql)
    mycursor.execute(sql)

mydb.commit()
f.close()
