const express = require("express")
const router = express.Router();
const annaAppItem = require('../models/AnnaGPT')
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

router.get('/annaApp',
  isLoggedIn,

  async function (req, res, next) {
    const showItems = req.query.showItems;
    items = await annaAppItem.find({ userId: req.user._id })
    res.render('annaApp', { items });
  });

router.post('/gpt',
  isLoggedIn,
  async (req, res, next) => {
    const language = req.body.userLanguage;
    const prompt = req.body.userInput;
    const response = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: "translate prompt: " + prompt + " to " + language + ":",
    });

    const request = new annaAppItem(
      {
        input: req.body.userInput,
        output: response.data.choices[0].text,
        createdAt: new Date(),
        userId: req.user._id
      })
    await request.save();
    res.redirect('/annaApp')
  });

router.get('/annaApp/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
    console.log("inside /annaApp/remove/:itemId")
    await annaAppItem.deleteOne({ _id: req.params.itemId });
    res.redirect('/annaApp')
  });

// router.get('/annaApp/complete/:itemId',
//   isLoggedIn,
//   async (req, res, next) => {
//     console.log("inside /annaApp/complete/:itemId")
//     await annaAppItem.findOneAndUpdate(
//       { _id: req.params.itemId },
//       { $set: { completed: true } });
//     res.redirect('/annaApp')
//   });

// router.get('/annaApp/uncomplete/:itemId',
//   isLoggedIn,
//   async (req, res, next) => {
//     console.log("inside /annaApp/complete/:itemId")
//     await annaAppItem.findOneAndUpdate(
//       { _id: req.params.itemId },
//       { $set: { completed: false } });
//     res.redirect('/annaApp')
//   });

// router.get('/annaApp/edit/:itemId',
//   isLoggedIn,
//   async (req, res, next) => {
//     console.log("inside /annaApp/edit/:itemId")
//     const item =
//       await annaAppItem.findById(req.params.itemId);
//     //res.render('edit', { item });
//     res.locals.item = item
//     res.render('edit')
//     //res.json(item)
//   });

// router.post('/annaApp/updateannaAppItem',
//   isLoggedIn,
//   async (req, res, next) => {
//     const { itemId, item, priority } = req.body;
//     console.log("inside /annaApp/complete/:itemId");
//     await annaAppItem.findOneAndUpdate(
//       { _id: itemId },
//       { $set: { item, priority } });
//     res.redirect('/annaApp')
//   });

module.exports = router;