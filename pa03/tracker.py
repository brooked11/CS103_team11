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

import sys
from transaction import Transaction

# here are some helper functions ...

def print_menu():
    ''' print an explanation of how to use this command '''
    print('''commands: usage
            0. quit : exits the program
            1. show : shows all transactions
            2. add amount category date description : adds a transaction
            3. delete transaction_id : deletes a transaction
            4. summarize date : summarizes transactions by their date
            5. summarize month MM : summarize transactions by their month
            6. summarize year YYYY: summarize transactions by their year
            7. summarize cat : summarize transactions by their category
            8. menu : print this menu
            '''
            )

def print_transactions(transactions):
    ''' print the transaction items '''
    if len(transactions)==0:
        print('no transactions to print')
        return
    print('\n')
    #print("%-10s %-10s %-10s %-10s %-10s"%('item #','amount','category','date','description'))
    print(f"{'item #':<10s}{'amount':<15s}{'category':<15s}{'date':<15s}{'description':<15s}")
    print('-'*50)
    for item in transactions:
        vals = tuple(item.values()) #('item #','amount','category','date','description')
        #print(f"%-10s %-10s %-10s %-10s %-10s"%values)
        print(f"{vals[0]:<10d}{vals[1]:<15.2f}{vals[2]:<15s}{vals[3]:<15s}{vals[4]:<15s}")

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    transaction_list = Transaction('tracker.db')
    if arglist==[]:
        print_menu()
    elif arglist[0]=="quit": # by Anna
        print("bye")
        sys.exit(0)
    elif arglist[0]=="show": # by Simon and Anna
        print_transactions(transaction_list.select_all())
    elif arglist[0]=="summarize":
        if len(arglist)<2: # not = because will mess up sum cat
            print_menu()
        elif arglist[1]=="month": # by Brooke
            print_transactions(transaction_list.sum_by_month(arglist[2])) #need to change
        elif arglist[1] == "date": # by Debbie
            print_transactions(transaction_list.sum_by_date())
        elif arglist[1]=="cat": # by Brooke
            print_transactions(transaction_list.sum_by_category())
        elif arglist[1]=="year": # by Anna
            print_transactions(transaction_list.sum_by_year(arglist[2]))
    elif arglist[0]=='add': # by Anna
        if len(arglist)!=5: #doesn't work if add is by itself
            print_menu()
        else:
            transaction = {'amount':arglist[1],'category':arglist[2],'date':arglist[3],
                            'description': arglist[4]}
            transaction_list.add(transaction)
    elif arglist[0]=='delete': # by Debbie
        if len(arglist)!= 2:
            print_menu()
        else:
            transaction_list.delete(arglist[1])
    elif arglist[0]=='menu': # by Simon
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
            print('-'*50+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*50+'\n'*3)

# this is the main function of the program
toplevel()

