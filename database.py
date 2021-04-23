# Import package 
import sqlite3

# Connect to the database 
conn = sqlite3.connect('customer.db')

# Create a cursor 
c = conn.cursor()

# List of customers 
customer_list = [

('Tom','Jones','Tom@jones.com'),
('Dick','Feynman','Dick@Feynman.com'),
('Jerry','Springer','Jerry@Springer.com'),

]
# Create a Table
c.executemany("INSERT INTO customers VALUES (?,?,?)",customer_list)

# Commit the command 
conn.commit()

# Now we close the connection. 
conn.close()

