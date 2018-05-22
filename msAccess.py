import pyodbc 
db_file = r'''Drive:\path\to\msaccess\DBname'''
user = 'user'
password = 'pass'
 
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' %\
                (db_file, user, password)

conn = pyodbc.connect(odbc_conn_str)
cursor = conn.cursor()
cursor.execute('select ID_EMP,NAME,SURNAME,SEX,SECTION, DEPARTMENT,POSITION from person ') 
for row in cursor.fetchall():
    print (row.ID_EMP,row.NAME,row.SURNAME,row.SEX,row.SECTION,row.DEPARTMENT,row.POSITION)
