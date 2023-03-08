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
        <h1>Home Page</h1>
        <nav>
            <a href="{url_for('about')}">About Us</a>
            <a href="{url_for('team')}">Team Members</a>
            <a href="{url_for('index')}">Index of Team Members' pages</a>
        </nav>
    '''

@app.route('/about')
def about():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>About Us</h1>
        <p>Our team is made up of 4 members: Anna, Brooke, Simon, and Debbie.</p>
        <br>
        <a href='/'>Home</a>
        
    '''

@app.route('/team')
def team():
    return f'''
    <h1>Team Members</h1>
    <br>
    <a href='/'>Home</a>
    '''

@app.route('/index')
def index():

    ''' displays link to the team members' pages '''
    return f'''
    <h1>Index of Team Members' pages</h1>

    <ul>
        <li><a href="{url_for('annaForm')}">Anna's GPT Method</a></li>
        <li><a href="{url_for('gptdemo')}">Ask questions to GPT</a></li>
        <li><a href="{url_for('simondemo')}">Simon's GPT Demo</a></li>
    </ul>
    <br>
    <a href='/'>Home</a>

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
        <a href={url_for('annaForm')}>Type more!</a>
        <br>
        <a href="{url_for('index')}">Go Back to Index</a>
        <br>
        <a href='/'>Home</a>
        '''
    else:
        return '''
        <h1>Anna's method</h1>
        Enter a text below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
@app.route('/simondemo', methods=['GET', 'POST'])
def simondemo():
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
        <a href={url_for('simondemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>Simon's GPT Demo App</h1>
        Enter your code below. The app will add comments to your code.
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
        <a href='/'>Home</a>
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