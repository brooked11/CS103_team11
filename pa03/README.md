# pylint script for transaction.py
```
************* Module transaction
transaction.py:23:54: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:33:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:37:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:46:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:54:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:57:0: C0301: Line too long (121/100) (line-too-long)
transaction.py:58:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:61:0: C0301: Line too long (122/100) (line-too-long)
transaction.py:62:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:67:26: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:63:29: W0622: Redefining built-in 'tuple' (redefined-builtin)

------------------------------------------------------------------
Your code has been rated at 5.94/10 (previous run: 5.94/10, +0.00)
```
# pylint script for tracker.py
```
************* Module tracker
tracker.py:102:41: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:121:0: C0305: Trailing newlines (trailing-newlines)
tracker.py:59:0: R0912: Too many branches (17/12) (too-many-branches)

------------------------------------------------------------------
Your code has been rated at 9.51/10 (previous run: 9.52/10, -0.02)
```
# pytest script for transaction.py
```
========================================================================== test session starts ==========================================================================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /mnt/c/Users/sthuy/cs103/CS103_team11/pa03
plugins: anyio-3.6.2
collected 7 items

test_transaction.py::test_add PASSED                                                                                                                              [ 14%]
test_transaction.py::test_sum_by_year PASSED                                                                                                                      [ 28%]
test_transaction.py::test_sum_by_month PASSED                                                                                                                     [ 42%]
test_transaction.py::test_delete PASSED                                                                                                                           [ 57%]
test_transaction.py::test_sum_by_date PASSED                                                                                                                      [ 71%]
test_transaction.py::test_sum_by_category PASSED                                                                                                                  [ 85%]
test_transaction.py::test_delete_all PASSED                                                                                                                       [100%]

=========================================================================== 7 passed in 2.05s ===========================================================================
```
# a script of running tracker.py and show all the added features
```
commands: usage
            0. quit : exits the program
            1. show : shows all transactions
            2. add amount category date description : adds a transaction
            3. delete transaction_id : deletes a transaction
            4. summarize date : summarizes transactions by their date
            5. summarize month MM : summarize transactions by their month
            6. summarize year YYYY: summarize transactions by their year
            7. summarize cat : summarize transactions by their category
            8. menu : print this menu

command> add 5.23 fishing 2023-03-26 fishing hooks
--------------------------------------------------



command> add 11.99 hiking 2019-06-25 hiking in Vermont
--------------------------------------------------



command> add 3.14 fishing 2019-03-11 fishing with pies
--------------------------------------------------



command> show


item #    amount         category       date           description
--------------------------------------------------
1         5.23           fishing        2023-03-26     fishing hooks
2         11.99          hiking         2019-06-25     hiking in Vermont
3         3.14           fishing        2019-03-11     fishing with pies
--------------------------------------------------



command> summarize date


item #    amount         category       date           description
--------------------------------------------------
3         3.14           fishing        2019-03-11     fishing with pies
2         11.99          hiking         2019-06-25     hiking in Vermont
1         5.23           fishing        2023-03-26     fishing hooks
--------------------------------------------------



command> summarize month 03


item #    amount         category       date           description    
--------------------------------------------------
3         3.14           fishing        2019-03-11     fishing with pies
1         5.23           fishing        2023-03-26     fishing hooks  
--------------------------------------------------



command> summarize year 2019


item #    amount         category       date           description    
--------------------------------------------------
3         3.14           fishing        2019-03-11     fishing with pies
2         11.99          hiking         2019-06-25     hiking in Vermont
--------------------------------------------------



command> delete 3
--------------------------------------------------



command> show


item #    amount         category       date           description
--------------------------------------------------
1         5.23           fishing        2023-03-26     fishing hooks
2         11.99          hiking         2019-06-25     hiking in Vermont
--------------------------------------------------



command> menu
commands: usage
            0. quit : exits the program
            1. show : shows all transactions
            2. add amount category date description : adds a transaction
            3. delete transaction_id : deletes a transaction
            4. summarize date : summarizes transactions by their date
            5. summarize month MM : summarize transactions by their month
            6. summarize year YYYY: summarize transactions by their year
            7. summarize cat : summarize transactions by their category
            8. menu : print this menu

--------------------------------------------------



command> quit
bye
```
