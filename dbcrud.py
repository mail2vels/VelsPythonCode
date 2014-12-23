print '''
    5. Build a library system with a CRUD option of book i.e. list, add, edit and delete. N.B. Create mysql table for doing this.
    (The app should run terminal)
'''

import MySQLdb

mydb = MySQLdb.connect("localhost", "root", "password", 'librarydb')

mydbcursor = mydb.cursor()

#Select Data from DB

sqlSelectQry = "SELECT * FROM book_details"
mydbcursor.execute(sqlSelectQry)
QryResults = mydbcursor.fetchall()
print('Showing Books Details')
print '======================\n'
for r in QryResults:
    print('Book Id : ' + str(r[0]))
    print('Book Name : ' + str(r[1]))
    print('Author of Book : ' + str(r[2]))
    print('Book Price : ' + str(r[3])+'\n')

#Insert Data to DB
print '\nInsert New Book Details Below'
print '===========================\n'
bookName = raw_input("Enter Book Name :  ")
authorOfBook = raw_input("Enter Author Of Book : ")
bookPrice = raw_input("Enter Book Price : ")
sqlInsertQry = "INSERT INTO book_details(bookName, authorOfBook, bookPrice) values(%s, %s, %s)"
mydbcursor.execute(sqlInsertQry, (bookName, authorOfBook, bookPrice))

#UPdate Data into DB
print '\nUpdate The Book Price Below'
print '=============================\n'
bookId = raw_input("Enter Book Id to update : ")
bookPrice = raw_input("Enter Book Price :  ")
sqlUpdateQry = "UPDATE book_details SET bookPrice =%s WHERE bookId = %s"
mydbcursor.execute(sqlUpdateQry, (bookPrice, bookId))

#Delete Data from DB
print '\nDelete The Particular Book Below'
print '=============================\n'
bookId = raw_input("Enter Book Id to Delete : ")
sqlDeleteQry = "DELETE FROM book_details WHERE bookId = %s"
mydbcursor.execute(sqlDeleteQry, (bookId))


#Select Data from DB After Insert, Update and Delete Operations
print 'Select Data from DB After Insert, Update and Delete Operations'
print '==============================================================\n'

sqlSelectQry2 = "SELECT * FROM book_details"
mydbcursor.execute(sqlSelectQry2)
QryResults = mydbcursor.fetchall()
print('Showing Books Details')
print '======================\n'
for r in QryResults:
    print('Book Id : ' + str(r[0]))
    print('Book Name : ' + str(r[1]))
    print('Author of Book : ' + str(r[2]))
    print('Book Price : ' + str(r[3])+'\n')

mydb.commit()
mydb.close()

