'''
transaction.py is an Object Relational Mapping to the tracker database

The ORM will work map SQL rows with the schema
    (itemid,amount,category,date,description)
to Python Dictionaries as follows:

(5,11.99,'personal','6/11/23','personal transaction') <-->
{itemid:5,amt:'11.99',cat:'personal',date:'6/11/23',desc:'personal transaction')

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database provided by the user,
or if none is provided, it will use the default database tracker.db

'''
import sqlite3
# import os

def toDict(t):
    ''' t is a tuple (rowid,amount,category,date,description)'''
    print('t='+str(t))
    transaction = {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transaction

class Transaction():
    def __init__(self, dbfile='tracker.db'):
        self.run_query('''CREATE TABLE IF NOT EXISTS 'transaction'
                    (amount double, category text, date text, description text)''',())
        
    def select_active(self):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        return self.run_query("SELECT rowid,* FROM 'transaction' WHERE amount>0",())
    
    def select_all(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.run_query("SELECT rowid,* from 'transaction'",())
    
    def add(self,item):
        ''' create a transaction item and add it to the 'transaction' table '''
        return self.run_query("INSERT INTO 'transaction' VALUES(?,?,?,?)",
                              (item['amount'],item['category'],item['date'],item['description']))
    
    def delete(self,item_id):
        ''' delete a 'transaction' item '''
        return self.run_query("DELETE FROM 'transaction' WHERE rowid=(?)",(item_id,))
    
    def sum_by_month(self):
        ''' summarize transactions by month '''
        return self.run_query("SELECT rowid,* FROM 'transaction' ORDER BY date",())
    
    def sum_by_category(self):
        ''' summarize transactions by category '''
        return self.run_query("SELECT rowid,* FROM 'transaction' ORDER BY category",())
    
    def run_query(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        #con= sqlite3.connect(os.getenv('HOME')+'/transaction.db')
        con = sqlite3.connect('tracker.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
    
    def delete_transaction(self,item_id):
        self.cursor.execute("DELETE FROM transactions WHERE rowid=?",(item_id,))
        self.conn.commit()
