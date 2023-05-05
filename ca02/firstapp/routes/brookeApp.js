/*
  todo.js -- Router for the ToDoList
*/
const express = require('express');
const router = express.Router();
const brookeAppItem = require('../models/BrookeGPT')
const User = require('../models/User')

// configure dotenv // install: npm install dotenv
require("dotenv").config();

// import modules from OpenAI library
const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});

const openai = new OpenAIApi(configuration);

/*
this is a very simple server which maintains a key/value
store using an object where the keys and values are lists of strings
*/

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

// get the value associated to the key
router.get('/brookeApp/',
  isLoggedIn,
  async (req, res, next) => {
      const show = req.query.show
    items = 
        await brookeAppItem.find({userId:req.user._id})
            res.render('brookeApp',{items});
});


/* add the value in the body to the list associated to the key */
router.post('/brookeGpt',
  isLoggedIn,
  async (req, res, next) => {
      const prompt = req.body.userInput;
      const response = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: "Insert comments into this code:" + prompt,
        max_tokens: 120,
      });
      const request = new brookeAppItem(
        {input:req.body.userInput,
         output: response.data.choices[0].text,
         createdAt: new Date(),
         userId: req.user._id
        })
      await request.save();
      res.redirect('/brookeApp')
});

router.get('/brookeApp/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /brookeApp/remove/:itemId")
      await brookeAppItem.deleteOne({_id:req.params.itemId});
      res.redirect('/brookeApp')
});

router.get('/brookeApp/complete/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /brookeApp/complete/:itemId")
      await brookeAppItem.findOneAndUpdate(
        {_id:req.params.itemId},
        {$set: {completed:true}} );
      res.redirect('/brookeApp')
});

router.get('/brookeApp/uncomplete/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /brookeApp/complete/:itemId")
      await brookeAppItem.findOneAndUpdate(
        {_id:req.params.itemId},
        {$set: {completed:false}} );
      res.redirect('/brookeApp')
});

router.get('/brookeApp/edit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /brookeApp/edit/:itemId")
      const item = 
       await brookeAppItem.findById(req.params.itemId);
      //res.render('edit', { item });
      res.locals.item = item
      res.render('edit')
      //res.json(item)
});

router.post('/brookeApp/updatebrookeAppItem',
  isLoggedIn,
  async (req, res, next) => {
      const {itemId,item,priority} = req.body;
      console.log("inside /brookeApp/complete/:itemId");
      await brookeAppItem.findOneAndUpdate(
        {_id:itemId},
        {$set: {item,priority}} );
      res.redirect('/brookeApp')
});

module.exports = router;