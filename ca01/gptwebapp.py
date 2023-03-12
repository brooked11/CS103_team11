'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def home():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1><ins>Team 11's Home Page</ins></h1>
        <nav>
            <button><h3><a href="{url_for('about')}">About Us</a></h3></button>  
            <button><h3><a href="{url_for('team')}">Team Members</a></h3></button>  
            <button><h3><a href="{url_for('index')}">Index of Team Members' pages</a></h3></button>
            <h4>Find Debbie on LinkedIn!</h4>
            <a href="https://www.linkedin.com/in/deborahengelberg/" target="_blank"><img src="https://raw.githubusercontent.com/nakulbhati/nakulbhati/master/contain/in.png" alt="LinkedIn" width="30"></a>
        </nav>
    '''

@app.route('/about')
def about():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>About Us</h1>
        <p>Hello, this is Team 11.</p>
        <p>Our team is made up of 4 members: Anna, Brooke, Simon, and Deborah.</p>
        <br>
        <button><b><a href='/'>Home</a></b></button>
        
    '''

@app.route('/team')
def team():
    return f'''
    <h1><header><ins>Team Members</ins><header></h1>
    <h2>Brooke</h2>
    Brooke is a sophomore at Brandeis. She created a method that looks at the code the user input and responds with what it does.
    <br><br>
    <h2>Anna</h2>
    Anna is a computer scientist.
    <br><br>
    <h2>Simon</h2>
    Simon has been studied math for a while now and wanted to learn a bit more coding. The form he created will add comments to the code the user inputs and make it more human-readble. 
    <br><br>
    <h2>Debbie</h2>
    Debbie is a computer scientist.
    <br><br><br>
    <button><b><a href='/'>Home</a></b></button>
    '''

@app.route('/index')
def index():

    ''' displays link to the team members' pages '''
    return f'''
    <h1>Index of Team Members' pages</h1>

    <ul>
        <li><a href="{url_for('annaForm')}">Anna's GPT Method</a></li>
        <li><a href="{url_for('simonForm')}">Simon's GPT Demo</a></li>
        <li><a href="{url_for('brookeForm')}">Brooke's GPT Demo</a></li>
        <li><a href="{url_for('deborahForm')}">Deborah's GPT Demo</a></li>

    </ul>
    <br>
    <button><b><a href='/'>Home</a></b></button>

    '''

@app.route('/annaform', methods=['GET', 'POST'])
def annaForm():
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.annaMethod(prompt)
        return f'''
        <h1>Anna's method</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer:
        <br>
        <div style="border:thin solid black; padding: 10px">{answer}</div>
        <br>
        <a href={url_for('annaForm')}>Type more!</a>
        <br>
        <a href="{url_for('index')}">Go Back to Index</a>
        <br>
        <button><b><a href='/'>Home</a></b></button>
        '''
    else:
        return '''
        <h1>Anna's method</h1>
        Enter a text below. The app will jumble it up!
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
@app.route('/simonForm', methods=['GET', 'POST'])
def simonForm():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getSimonResponse(prompt)
        return f'''
        <h1>Simon's GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('simonForm')}> make another query</a>
        <br>
        <a href="{url_for('index')}">Go Back to Index</a>
        <br>
        <button><b><a href='/'>Home</a></b></button>
        '''
    else:
        return '''
        <h1>Simon's GPT Demo App</h1>
        Enter your your program below. This app will add comments to your code and make it more human-readable.
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/brookeform', methods=['GET', 'POST'])
def brookeForm():
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.brookeMethod(prompt)
        return f'''
        <h1>Brooke's method</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('brookeForm')}>Type more!</a>
        <br>
        <a href="{url_for('index')}">Go Back to Index</a>
        <br>
        <button><b><a href='/'>Home</a></b></button>
        '''
    else:
        return '''
        <h1>Brooke's method</h1>
        Submit a program and I'll tell you what it does.
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
@app.route('/deborahform', methods=['GET', 'POST'])
def deborahForm():
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.deborahMethod(prompt)
        return f'''
        <h1>Deborah's method</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer:
        <br>
         <pre style="border:thin solid black">{answer}</pre>
        <br>
        <a href={url_for('deborahForm')}>Type more!</a>
        <br>
        <a href="{url_for('index')}">Go Back to Index</a>
        <br>
        <button><b><a href='/'>Home</a></b></button>
        '''
    else:
        return '''
        <h1>Deborah's method</h1>
         Enter your your program below. This app will rewrite it in Java!! Enjoy :)
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        <br>
        <button><b><a href='/'>Home</a></b></button>
        '''                          
    
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    


if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)