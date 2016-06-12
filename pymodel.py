#import torndb
import MySQLdb as _mysql

# DB = torndb.Connection('localhost','one',user='root',password='1q2w3e4r')
#
# a = DB.query('select * from onethink_action')
# print a[0]['status']


# DB = mdb.Connect(host='localhost',db='one',user='root',passwd='1q2w3e4r',port=3306)
#
# cursor = DB.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print data
#
# cursor.execute('DROP TABLE IF EXISTS ANC')
# sql = '''CREATE TABLE ANC(
#         first_name CHAR(20) NOT NULL,
#         last_name char(20),
#         age int,
#         sex char(1),
#         income float)
# '''
# cursor.execute(sql)
#
# insql ='''insert into ANC value ('%s','%s','%d','%c','%d') ''' % ('changwei','su',25,'M',2000)
#
# try:
#     cursor.execute(insql)
#     DB.commit()
#     print 'OK'
# except:
#     DB.rollback()
#
# cursor.execute('select * from ANC')
# newda = cursor.fetchone()
# print newda
#
# try:
#     cursor.execute('select * from onethink_action')
#     results = cursor.fetchall()
#     for re in results:
#         print re
# except:
#     print 'Error: unable to fetch data'
#
# DB.close()
dbconfig = dict(
    host='localhost',
    db='one',
    user='root',
    passwd='1q2w3e4r',
    port=3306
)

db = _mysql.connect(**dbconfig)
conn = db.cursor()
# print conn.execute('SELECT VERSION()')
sql='select * from onethink_action'
try:
    conn.execute(sql)
    for re in conn.fetchall():
        print re[0]
except:
    print 'No...'
conn.close()
conn.execute('select version()')
db.close()