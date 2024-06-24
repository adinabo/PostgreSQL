import psycopg2

#connect to chinook
connection = psycopg2.connect(database = "chinook")


#build a cursor of the database/ array in Js


#fetch data from cursor/ multiple
results=cursor.fetchall()

#Query1 select all records from Artist table
cursor.execute('SELECT * FROM "Artist"')

#fetch data from cursor/ one
# results=cursor.fetchone()

#close connection
connection.close()

#print results
for result in results:
    print(result)