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

def to_dict(item):
    ''' t is a tuple (rowid,amount,category,date,description)'''
    #print('item='+str(item)) # transaction.py should not print anything; this is for debugging
    transaction = {'item #':item[0], 'amount':item[1], 
                   'category':item[2], 'date':item[3], 'description':item[4]}
    return transaction

class Transaction():
    ''' ORM for the tracker database'''
    def __init__(self, db_file): # by Simon
        self.db_file = db_file
        self.run_query('''CREATE TABLE IF NOT EXISTS 'transaction'
                    (amount double, category text, date text, description text)''',())
    
    def select_all(self): # by everyone
        ''' return all of the transactions as a list of dicts.'''
        return self.run_query("SELECT rowid,* from 'transaction'",())
    
    def add(self,item): # by Anna
        ''' create a transaction item and add it to the 'transaction' table '''
        return self.run_query("INSERT INTO 'transaction' VALUES(?,?,?,?)",
                              (item['amount'],item['category'],item['date'],item['description']))
    
    def delete(self,item_id): # by Debbie
        ''' delete a 'transaction' item '''
        return self.run_query("DELETE FROM 'transaction' WHERE rowid=(?)",(item_id,))
    
    def sum_by_date(self): # by Debbie
        ''' summarize transactions by date '''
        return self.run_query("SELECT rowid,* FROM 'transaction' ORDER BY date",())
    
    def sum_by_category(self): # by Brooke
        ''' summarize transactions by category '''
        return self.run_query("SELECT rowid,* FROM 'transaction' ORDER BY category",())
    
    def sum_by_year(self, year): # by Anna
        ''' summarize transactions by year '''
        return self.run_query("SELECT rowid,* FROM 'transaction' WHERE strftime('%Y', date)=(?) ORDER BY date ", (year,))
    
    def sum_by_month(self, month): # by Brooke
        ''' summarize transactions by year '''
        return self.run_query("SELECT rowid,* FROM 'transaction' WHERE strftime('%m', date)=(?) ORDER BY date ", (month,))
    
    def run_query(self,query,tuple):
        ''' return all of the transactions as a list of dicts.'''
        #con= sqlite3.connect(os.getenv('HOME')+'/transaction.db')
        con = sqlite3.connect(self.db_file)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]

    ### for testing purposes only ###
    # by Simon and Anna
    def delete_all(self):
        ''' delete all of the transactions '''
        return self.run_query("DELETE FROM 'transaction'",())
