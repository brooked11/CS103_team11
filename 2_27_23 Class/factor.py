'''
  this demo shows how to pass data to and from a flask server
'''
from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <h1>Flask Demo</h1>
    <ul>
      <li><a href="/factors_of/120">factors of 120</a></li>
      <li><a href="/factor_demo">factor demo</a></li>
    </ul>
    '''

@app.route('/factors_of/<num>')
def factors_of(num):
    num=int(num)
    factors = [d for d in range(1,num+1) if num%d==0]
    return factors

@app.route('/factor_demo', methods=['GET', 'POST'])
def factor_demo():
    if request.method == 'GET':
        return '''
        <form method="POST" action="/factor_demo">
          Enter a number to factor: <input type="text" name="num"><br>
          <input type="submit">
        </form>
        '''
    elif request.method == 'POST':
        num=int(request.form['num'])
        factors = [d for d in range(1,num+1) if num%d==0]
        return factors
    else:
        return 'unknown HTTP method: '+str(request.method)

@app.route('/prime/<num>')
def prime(num):
    num=int(num)
    factors = [d for d in range(1,num+1) if num%d==0]
    if len(factors)==2:
        return 'true'
    else:
        return 'false'

@app.route('/prime_demo', methods=['GET', 'POST'])
def prime_demo():
    if request.method == 'GET':
        return '''
        <form method="POST" action="/prime_demo">
          Enter a number to check if prime: <input type="text" name="num"><br>
          <input type="submit">
        </form>
        '''
    elif request.method == 'POST':
        num=int(request.form['num'])
        factors = [d for d in range(1,num+1) if num%d==0]
        if len(factors)==2:
            return 'true'
        else:
            return 'false'
    else:
        return 'unknown HTTP method: '+str(request.method)

@app.route('/powers')
def powers():
    powers = [2**d for d in range(0,10)]
    return powers

@app.route('/power_demo', methods=['GET', 'POST'])
def power_demo():
    if request.method == 'GET':
        return '''
        <form method="POST" action="/power_demo">
          Enter a number to find powers: <input type="text" name="num"><br>
          <input type="submit">
        </form>
        '''
    elif request.method == 'POST':
        num=int(request.form['num'])
        powers = [2**d for d in range(0,num+1)]
        return powers
    else:
        return 'unknown HTTP method: '+str(request.method)

if __name__=='__main__':
    app.run(debug=True,port=5001)
