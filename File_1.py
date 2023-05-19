import mysql.connector as jing
mycon=jing.connect(host="localhost",user="root",passwd="*****",database="****")
if mycon.is_connected():
print("SUCCESSFUL")

cursor=mycon.cursor()
st6="DROP TABLE Personal;"
cursor.execute(st6)
mycon.commit()
mycon.close()
