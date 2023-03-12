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
        <header style="text-align: center; color: silver; background-color: #02437B; border: 4px solid silver; padding: 13px"><h1><ins>Team 11's Home Page</ins></h1></header>
        <nav>
            <button><h3><a href="{url_for('about')}">About Us</a></h3></button>  
            <button><h3><a href="{url_for('team')}">Team Members</a></h3></button>  
            <button><h3><a href="{url_for('index')}">Index of Team Members' pages</a></h3></button>
            <h4>Find Debbie on LinkedIn below!</h4>
            <a href="https://www.linkedin.com/in/deborahengelberg/" target="_blank"><img src="https://raw.githubusercontent.com/nakulbhati/nakulbhati/master/contain/in.png" alt="LinkedIn" width="30"></a>
            <h4>Find Anna on LinkedIn below!</h4>
            <a href="https://www.linkedin.com/in/anna-kolb-745a38233/" target="_blank"><img src="https://raw.githubusercontent.com/nakulbhati/nakulbhati/master/contain/in.png" alt="LinkedIn" width="30"></a>
            <h4>Find Simon on LinkedIn below!</h4>
            <a href="https://www.linkedin.com/in/sthuynh11/" target="_blank"><img src="https://raw.githubusercontent.com/nakulbhati/nakulbhati/master/contain/in.png" alt="LinkedIn" width="30"></a>
            <h4>Find Brooke on LinkedIn below!</h4>
            <a href="https://www.linkedin.com/in/brooke-schwartz-456680135/" target="_blank"><img src="https://raw.githubusercontent.com/nakulbhati/nakulbhati/master/contain/in.png" alt="LinkedIn" width="30"></a>
             </nav>
    '''

@app.route('/about')
def about():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <header style="text-align: center; color: silver; background-color: #02437B; border: 4px solid silver; padding: 13px"><h1><ins>About Us</ins></h1></header>
        <p>Hello, this is Team 11.</p>
        <p>Our team is made up of 4 members: Anna, Brooke, Simon, and Debbie.</p>
        <section style="display: flex; flex-wrap: wrap">
            <article style="flex: 1; border: 4px solid black; padding: 10px">
                <h4><u>Anna's Program</u></h4>
                <p>
                    Anna's program is a method that takes in a random prompt (a sentence or single word)
                    and returns a jumbled up response. Jumbled up/mixed up means either adding or removing letters/words
                    to the original prompt.
                </p>
            </article>
            <article style="flex: 1; border: 4px solid black; padding: 10px">
                <h4><u>Brooke's Program</u></h4>
                <p>
                    Type program info here
                </p>
            </article>
            <article style="flex: 1; border: 4px solid black; padding: 10px">
                <h4><u>Simon's Program</u></h4>
                <p>
                    Type program info here
                </p>
            </article>
            <article style="flex: 1; border: 4px solid black; padding: 10px">
                <h4><u>Debbie's Program</u></h4>
                <p>
                    Type program info here
                </p>
            </article> 
        </section>        
        <br>
        <button><b><a href='/'>Home</a></b></button>
        
    '''

@app.route('/team')
def team():
    return f'''
    <header style="text-align: center; color: silver; background-color: #02437B; border: 4px solid silver; padding: 13px"><h1><ins>Team Members</ins></h1></header>
    <h2>Brooke</h2>
    Brooke is a sophomore at Brandeis. She created a method that looks at the code the user input and responds with what it does.
    <br><br>
    <h2>Anna</h2>
    Anna is a sophomore at Brandeis majoring in computer scientist and minoring in architecture. Her job on the team
    was to create her own method for the project, as well as start the layouts of all preceedings. She copied and
    uploaded the gpt.app and gptwebapp.py files to our repository as well as the project instructions/directions. 
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
    <header style="text-align: center; color: silver; background-color: #02437B; border: 4px solid silver; padding: 13px"><h1><ins>Index of Team Members' pages</ins></h1></header>

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
        Here is the mix up!:
        <br>
        <div style="border:thin solid black; padding: 10px">{answer}</div>
        <br>
        <button><a href={url_for('annaForm')}>Type more!</a></button>
        <br>
        <button><a href="{url_for('index')}">Go Back to Index</a></button>
        <br>
        <button><b><a href='/'>Home</a></b></button>
        '''
    else:
        return '''
        <h1>Anna's method</h1>
        Enter your preferred language before the comma, then any word/sentence you wish to translate into that
        language!
        <form method="post">
            <textarea name="prompt" style="height: 200px; width: 400px"></textarea>
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
        <button><a href={url_for('simonForm')}> make another query</a></button>
        <br>
        <button><a href="{url_for('index')}">Go Back to Index</a></button>
        <br>
        <button><b><a href='/'>Home</a></b></button>
        '''
    else:
        return '''
        <h1>Simon's GPT Demo App</h1>
        Enter your your program below. This app will add comments to your code and make it more human-readable.
        <form method="post">
            <textarea name="prompt" style="height:200px;width=500px;"></textarea>
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
        <button><a href={url_for('brookeForm')}>Type more!</a></button>
        <br>
        <button><a href="{url_for('index')}">Go Back to Index</a></button>
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