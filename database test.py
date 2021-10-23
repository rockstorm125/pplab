import cx_Oracle

conn  = cx_Oracle.connect("system","123")
cursor = conn.cursor()
if conn!= None:
    print(conn)
else:
    print("not logged in")


