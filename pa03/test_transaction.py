'''Use pytest to test the transaction module'''

from transaction import Transaction

# def test_add():
#     '''test the add method'''
#     transaction_list = Transaction()
#     transaction = {'amount':11,'category':'food','date':'2019-01-01',
#                         'description': 'test'}

#     transaction_list.add(transaction)
#     # note that transaction_list.select_active() is a list of dictionaries
#     # transaction_list.select_active()[-1] is the last transaction in the list
#     assert transaction_list.select_active()[-1]['amount'] == 11
#     assert transaction_list.select_active()[-1]['category'] == 'food'
#     assert transaction_list.select_active()[-1]['date'] == '2019-01-01'
#     assert transaction_list.select_active()[-1]['description'] == 'test'
#     #transaction_list.delete(transaction_list.select_active()[-1]['item #'])
    
# def test_sum_by_year():
#     '''test the sum_by_year method'''
#     transaction_list = Transaction()

#     t2 = {'amount':20,'category':'war','date':'2010-12-16',
#                         'description': 'Canteen'}
#     t3 = {'amount':3.5,'category':'media','date':'2017-03-14',
#                         'description': 'Wii remote'}
#     t4 = {'amount':4.74,'category':'supply','date':'2010-02-27',
#                         'description': 'Pens'}
#     t5 = {'amount':5.00,'category':'food','date':'2017-01-19',
#                         'description': 'Bread'}    
    
#     transaction_list.add(t2)
#     transaction_list.add(t3)
#     transaction_list.add(t4)
#     transaction_list.add(t5)

#     assert transaction_list.sum_by_year('2010') == [{'item #': 4, 'amount': 4.74, 'category': 'supply', 'date': '2010-02-27', 'description': 'Pens'}, {'item #': 2, 'amount': 20.0, 'category': 'war', 'date': '2010-12-16', 'description': 'Canteen'}]
#     assert transaction_list.sum_by_year('2017') == [{'item #': 5, 'amount': 5.0, 'category': 'food', 'date': '2017-01-19', 'description': 'Bread'}, {'item #': 3, 'amount': 3.5, 'category': 'media', 'date': '2017-03-14', 'description': 'Wii remote'}]

def test_delete_all():
    '''test the delete_all method'''
    transaction_list = Transaction()
    transaction_list.delete_all()
    assert transaction_list.select_active() == []