const router = require("express").Router();

router.get('/annaApp', function(req, res, next) {
    res.render('annaApp');
});

////////////////////////////////////////////////////////////////////////

// router.post('/gpt', async (req,res,next) => {
//     const userInput = req.body.userInput;

//     const gptResponse = await openai.createCompletion({
//         model: "text-davinci-003",
//         prompt: "User input",
//     });

//     const completion = gptResponse.data.choices[0].text;

//     return res.status(200).json({
//         sucess: true,
//         message: completion,

//     });
// });

//////////////////////////////////////////////////////////

const openai = require('openai');
const openaiApiKey = 'YOUR_API_KEY';

router.get('/gpt', function(req, res, next) {
    const generateGptResponse = async (modelEngine, prompt) => {
        const openaiClient = new openai.OpenAI({apiKey: openaiApiKey});
      
        const response = await openaiClient.completions.create({
          engine: modelEngine,
          prompt: `translate statement after comma into language inputted before comma ${prompt}`,
          maxTokens: 1024,
          n: 1,
          stop: null,
          temperature: 0.8,
        });

        res.send(response);
      
        return response.choices[0].text;
      }
});

module.exports = router;