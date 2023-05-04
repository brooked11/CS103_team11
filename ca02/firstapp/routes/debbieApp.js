const express = require("express")
const router = express.Router();
const debbieAppItem = require('../models/DebbieGPT')
const User = require('../models/User')

require("dotenv").config();

const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});

const openai = new OpenAIApi(configuration);

isLoggedIn = (req, res, next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

router.get('/debbieApp',
  isLoggedIn,

  async function (req, res, next) {
    const showItems = req.query.showItems;
    items = await debbieAppItem.find({ userId: req.user._id })
    res.render('debbieApp', { items });
  });

router.post('/debbiegpt',
  isLoggedIn,
  async (req, res, next) => {
    
    const prompt = req.body.userInput;
    const response = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: "rewrite the inputted program in the java programming language, make sure to include the proper indentations and spacing" + prompt,
    });

    const request = new debbieAppItem(
      {
        input: req.body.userInput,
        output: response.data.choices[0].text,
        createdAt: new Date(),
        userId: req.user._id
      })
    await request.save();
    res.redirect('/debbieApp')
  });

router.get('/debbieApp/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
    console.log("inside /debbieApp/remove/:itemId")
    await debbieAppItem.deleteOne({ _id: req.params.itemId });
    res.redirect('/debbieApp')
  });

  module.exports = router;



