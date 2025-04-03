# File Name : main.py
# Student Name: Collin Baines / Connor Thomas
# email: bainesct@mail.uc.edu / thoma5cg@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   04/03/2025
# Course #/Section:   4010-0
# Semester/Year:   Spring/2025
# Brief Description of the assignment:  This assignment is to manipulate data in sql server using python/visualstudio

# Brief Description of what this module does. This module fetches data from the GroceryStoreSimulator and manipulates it
# Citations: 

# Anything else that's relevant:
 
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=GroceryStoreSimulator;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

# Question 1
cursor = conn.cursor()
cursor.execute('SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct')

# Question 2
rows = cursor.fetchall()
rowChoice = rows[3]
Description = rowChoice.Description
ProductID = rowChoice.ProductID
ManufacturerID = rowChoice.ManufacturerID
BrandID = rowChoice.BrandID

# print("ManufacturerID: ", + ManufacturerID) = 55
# print("BrandID: ", + BrandID) = 120
# print("ProductID: ", + ProductID) = 5


# Question 3
cursor = conn.cursor()
cursor.execute('SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = 55')

# Question 4
for row in cursor:
    manufacturerName = row

# Question 5
cursor = conn.cursor()
cursor.execute('SELECT Brand FROM tBrand WHERE BrandID = 120')
for row in cursor:
    brandName = row

# Question 6
cursor = conn.cursor()
cursor.execute('''
    SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
    FROM dbo.tTransactionDetail INNER JOIN
    dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID WHERE 
    (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = 5)
''')
result = cursor.fetchone()
numberOfItemsSold = result[0] if result and result[0] is not None else 0

# Question 7
sentence = f"The product '{Description}' made by {manufacturerName[0]} under the {brandName[0]} brand sold {numberOfItemsSold:,} units."
print(sentence)













