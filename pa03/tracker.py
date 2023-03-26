'''
tracker.py is an app that maintains a transaction list.

but it also uses an Object Relational Mapping (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Transaction, will map SQL rows with the schema
    (rowid,amount,category,date,description)

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database tracker.db

Recall that sys.argv is a list of strings capturing the
command line invocation of this program
sys.argv[0] is the name of the script invoked from the shell
sys.argv[1:] is the rest of the arguments (after arg expansion!)

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''

from transaction import Transaction
import sys

# here are some helper functions ...

def print_menu():
    ''' print an explanation of how to use this command '''
    print('''menu of available commands:
            0. quit : exit the program
            1. show transactions
            2. add transaction
            3. delete transaction
            4. summarize transactions by date
            5. summarize transactions by month
            6. summarize transactions by year
            7. summarize transactions by category
            8. menu : print this menu
            '''
            )

def print_transactions(transactions):
    ''' print the transaction items '''
    if len(transactions)==0:
        print('no tasks to print')
        return
    print('\n')
    #print("%-10s %-10s %-10s %-10s %-10s"%('item #','amount','category','date','description'))
    print(f"{'item #':<10s} {'amount':<10s} {'caterogy':<10s} {'date':<10s} {'description':<10s}")
    print('-'*60)
    for item in transactions:
        values = tuple(item.values()) #('item #','amount','category','date','description')
        #print(f"%-10s %-10s %-10s %-10s %-10s"%values)
        print(f"{values[0]:<10d} {values[1]:<10.2f} {values[2]:<10s} {values[3]:<10s} {values[4]:<10s}")

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    transaction_list = Transaction()
    if arglist==[]:
        print_menu()
    elif arglist[0]=="quit":
        print("bye")
        sys.exit(0)
    elif arglist[0]=="show":
        print_transactions(transaction_list.select_active())
    elif arglist[0]=="showall":
        print_transactions(transactions = transaction_list.select_all())
    elif arglist[0]=="sumbymonth":
        print_transactions(transaction_list.sum_by_month())
    elif arglist[0]=="sumbycategory":
        print_transactions(transaction_list.sum_by_category())
    elif arglist[0]=='add':
        if len(arglist)!=5: #doesn't work if add is by itself
            print_menu()
        else:
            transaction = {'amount':arglist[1],'category':arglist[2],'date':arglist[3],
                            'description': arglist[4]}
            transaction_list.add(transaction)
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_menu()
        else:
            transaction_list.delete(arglist[1])
    elif arglist[0]=='menu':
        print_menu()
    else:
        print(arglist,"is not implemented")
        print_menu()


def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_menu()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                # join everything after the name as a string
                args = ['add',args[1],args[2],args[3]," ".join(args[4:])]
            process_args(args)
            print('-'*60+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*60+'\n'*3)

# this is the main function of the program
toplevel()

