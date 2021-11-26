import sqlite3
# create and connect to database
connection = sqlite3.connect('chatbot.db')

# create a cursor
cursor = connection.cursor()

# create a table
# cursor.execute("""CREATE TABLE hospitals(
#                       name text,
#                       operational_hours text,
#                       address text,
#                       direction text,
#                       phone_number text
# )""")

# cursor.execute("""CREATE TABLE diseases(
#                       name text,
#                       cause text,
#                       treatment text,
#                       preventative_measure text
# )""")

#  insert values
# name = "Sean"
# number = "13372007893"
# cursor.execute("INSERT INTO userdetails VALUES (?,?)",(name,number))

# cursor.execute("SELECT * FROM hospitals")
# items = cursor.fetchall()

disease = "Stroke"
cursor.execute("SELECT * FROM diseases WHERE NAME = ?", (disease,))  # 看教程.
items = cursor.fetchall()

for item in items:
    # print(item)
    s= str(item).split('\'')
    list = s[1] + '\n'+"causes:" +'\n'+ s[3] +'\n' +"treatments:" +'\n'+s[5] +'\n' +"preventative measures:"+'\n'+s[7]
    # print(s[1])
    print(list)

connection.commit()
connection.close()

