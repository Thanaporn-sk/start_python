import cx_Oracle
import xlwt

host ='ip.ip.ip.ip'
port=1521
sid='sid'
user ='user'
password='password'
dsn = cx_Oracle.makedsn(host, port, sid)
conn = cx_Oracle.connect(user, password, dsn)

# query and write into sheet
def query2sheet(ws,sqlstr):  
    
    cursor = conn.cursor()
    cursor.execute(sqlstr) 
    row_id = 0
    rows = cursor.fetchall()
    rowscount= len(cursor.description)
    columns = [column[0] for column in cursor.description]
    # column header 
    for c in range(0,rowscount) :
        ws.write(0,c,columns[c])
    # data iteration
    for row in rows :
        row_id += 1
        for col in range(0,rowscount):
            ws.write(row_id,col,  row[col])            

#### end of query2sheet


wb = xlwt.Workbook()
ws = wb.add_sheet('temp_temp_table') # create new sheet : 
sqlstr = 'select * from temp_table'
query2sheet(ws,sqlstr)
wb.save('temp_table.xls')
#print (db)
