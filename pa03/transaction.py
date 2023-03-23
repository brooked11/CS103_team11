'''
todolist.py is an Object Relational Mapping to the todolist database

The ORM will work map SQL rows with the schema
    (rowid,title,desc,completed)
to Python Dictionaries as follows:

(5,'commute','drive to work',false) <-->
{rowid:5,title:'commute',desc:'drive to work',completed:false)

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

'''
import sqlite3
import os

def toDict(t):
    ''' t is a tuple (rowid,title, desc,completed)'''
    print('t='+str(t))

    #fields?
    todo = {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return todo

class Transaction():
    def __init__(self, dbfile='tracker.db'):
        self.runQuery('''CREATE TABLE IF NOT EXISTS 'transaction'
                    (amount double, category text, date text, description text)''',())
        
    def addCategory(self, item):
        return self.runQuery("INSERT INTO categories VALUES(?)",(item['categoryName']))
    
    def selectActive(self):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* FROM 'transaction' WHERE amount>0",())

    def selectAll(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from 'transaction'",())

    def selectCompleted(self):
        ''' return all of the completed tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from 'transaction' where completed=1",())

    def add(self,item):
        ''' create a todo item and add it to the 'transaction' table '''
        return self.runQuery("INSERT INTO 'transaction' VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))

    def delete(self,Id):
        ''' delete a 'transaction' item '''
        return self.runQuery("DELETE FROM 'transaction' WHERE Id=(?)",(Id,))

    def setComplete(self,Id):
        ''' mark a 'transaction' item as completed '''
        return self.runQuery("UPDATE 'transaction' SET completed=1 WHERE Id=(?)",(Id,))
    
    def refresh(self, Id):
        return self.runQuery("Refresh 'transaction' SET completed=0 WHERE rowid=(?)",(Id,))

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        #con= sqlite3.connect(os.getenv('HOME')+'/transaction.db')
        con = sqlite3.connect('tracker.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
    
    def delete_transaction(self, Id):
        self.cursor.execute("DELETE FROM transactions WHERE id=?",(Id,))
        self.conn.commit()
