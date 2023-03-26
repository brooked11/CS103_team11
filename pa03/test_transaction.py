'''Use pytest to test the transaction module'''

from transaction import Transaction

def test_add(): # by Simon
    '''test the add method'''
    transaction_list = Transaction('tracker.db')
    transaction = {'amount':11,'category':'food','date':'2019-01-01',
                        'description': 'test'}

    transaction_list.add(transaction)
    # note that transaction_list.select_all() is a list of dictionaries
    # transaction_list.select_all()[-1] is the last transaction in the list
    assert transaction_list.select_all()[-1]['amount'] == 11
    assert transaction_list.select_all()[-1]['category'] == 'food'
    assert transaction_list.select_all()[-1]['date'] == '2019-01-01'
    assert transaction_list.select_all()[-1]['description'] == 'test'
    #transaction_list.delete(transaction_list.select_all()[-1]['item #'])
    
def test_sum_by_year(): # by Anna and Simon
    '''test the sum_by_year method'''
    transaction_list = Transaction('tracker.db')

    t2 = {'amount':20,'category':'war','date':'2010-12-16',
                        'description': 'Canteen'}
    t3 = {'amount':3.5,'category':'media','date':'2017-03-14',
                        'description': 'Wii remote'}
    t4 = {'amount':4.74,'category':'supply','date':'2010-02-27',
                        'description': 'Pens'}
    t5 = {'amount':5.00,'category':'food','date':'2017-01-19',
                        'description': 'Bread'}    
    
    transaction_list.add(t2)
    transaction_list.add(t3)
    transaction_list.add(t4)
    transaction_list.add(t5)

    assert transaction_list.sum_by_year('2010') == [{'item #': 4, 'amount': 4.74, 'category': 'supply', 'date': '2010-02-27', 'description': 'Pens'}, {'item #': 2, 'amount': 20.0, 'category': 'war', 'date': '2010-12-16', 'description': 'Canteen'}]
    assert transaction_list.sum_by_year('2017') == [{'item #': 5, 'amount': 5.0, 'category': 'food', 'date': '2017-01-19', 'description': 'Bread'}, {'item #': 3, 'amount': 3.5, 'category': 'media', 'date': '2017-03-14', 'description': 'Wii remote'}]

def test_sum_by_month(): # by Brooke
    '''test the sum_by_month method'''
    transaction_list = Transaction('tracker.db')

    t6 = {'amount':6.74,'category':'food','date':'2010-05-27',
                        'description': 'Pens'}
    t7 = {'amount':7.00,'category':'supply','date':'2019-05-19',
                        'description': 'Bread'}
    
    transaction_list.add(t6)
    transaction_list.add(t7)

    assert transaction_list.sum_by_month('05') == [{'item #': 6, 'amount': 6.74, 'category': 'food', 'date': '2010-05-27', 'description': 'Pens'}, {'item #': 7, 'amount': 7.0, 'category': 'supply', 'date': '2019-05-19', 'description': 'Bread'}]

def test_delete(): # by Debbie
    '''test the delete method'''
    transaction_list = Transaction('tracker.db')
 
    transaction_list.delete(5)
    transaction_list.delete(3)
    transaction_list.delete(2)
    assert transaction_list.select_all() == [{'item #': 1, 'amount': 11.0, 'category': 'food', 'date': '2019-01-01', 'description': 'test'},
                                                {'item #': 4, 'amount': 4.74, 'category': 'supply', 'date': '2010-02-27', 'description': 'Pens'},
                                                {'item #': 6, 'amount': 6.74, 'category': 'food', 'date': '2010-05-27', 'description': 'Pens'},
                                                {'item #': 7, 'amount': 7.0, 'category': 'supply', 'date': '2019-05-19', 'description': 'Bread'}]

def test_sum_by_date(): # by Debbie
    '''test the sum_by_date method'''
    transaction_list = Transaction('tracker.db')

    assert transaction_list.sum_by_date() == [{'item #': 4, 'amount': 4.74, 'category': 'supply', 'date': '2010-02-27', 'description': 'Pens'}, 
                                                          {'item #': 6, 'amount': 6.74, 'category': 'food', 'date': '2010-05-27', 'description': 'Pens'},
                                                          {'item #': 1, 'amount': 11.0, 'category': 'food', 'date': '2019-01-01', 'description': 'test'},
                                                          {'item #': 7, 'amount': 7.0, 'category': 'supply', 'date': '2019-05-19', 'description': 'Bread'}]

def test_sum_by_category(): # by Brooke
   '''test the sum_by_category method'''
   transaction_list = Transaction('tracker.db')
   
   assert transaction_list.sum_by_category() == [{'item #': 1, 'amount': 11.0, 'category': 'food', 'date': '2019-01-01', 'description': 'test'},
                                                  {'item #': 6, 'amount': 6.74, 'category': 'food', 'date': '2010-05-27', 'description': 'Pens'},
                                                  {'item #': 4, 'amount': 4.74, 'category': 'supply', 'date': '2010-02-27', 'description': 'Pens'},
                                                  {'item #': 7, 'amount': 7.0, 'category': 'supply', 'date': '2019-05-19', 'description': 'Bread'}]


def test_delete_all(): # by Anna and Simon
    '''test the delete_all method'''
    transaction_list = Transaction('tracker.db')
    transaction_list.delete_all()
    assert transaction_list.select_all() == []