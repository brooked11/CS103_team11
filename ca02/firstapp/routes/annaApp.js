const router = require("express").Router();

// async function annaMethod(modelEngine, prompt) {
//     const openai = require('openai');

//     try {
//         const completion = await openai.Completion.create({
//             engine: modelEngine,
//             prompt: `translate statement after comma into language inputted before comma ${prompt}`,
//             max_tokens: 1024,
//             n: 1,
//             stop: null,
//             temperature: 0.8,
//         });

//         const response = completion.choices[0].text;
//         return response;
//     } catch (error) {
//         console.error(error);
//         return null;
//     }
// }

// router.get("/annaApp", (req, res, next) => {
//     res.render("annaApp");
//     }
// );

// module.exports = annaMethod;

// app.route('/annaform', methods=['GET', 'POST'])
// async function annaForm():
//     if request.method == 'POST':
//         prompt = request.form['prompt']
//         answer = gptAPI.annaMethod(prompt)
//         return f'''
//         <h1>Anna's method</h1>
//         <pre style="bgcolor:yellow">{prompt}</pre>
//         <hr>
//         Here is the answer:
//         <br>
//         <div style="border:thin solid black; padding: 10px">{answer}</div>
//         <br>
//         <a href={url_for('annaForm')}>Type more!</a>
//         <br>
//         <a href="{url_for('index')}">Go Back to Index</a>
//         <br>
//         <button><b><a href='/'>Home</a></b></button>
//         '''
//     else:
//         return '''
//         <h1>Anna's method</h1>
//         Enter a text below. The app will jumble it up!
//         <form method="post">
//             <textarea name="prompt"></textarea>
//             <p><input type=submit value="get response">
//         </form>
//         '''