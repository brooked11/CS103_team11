/*
  todo.js -- Router for the ToDoList
*/
const express = require('express');
const router = express.Router();
const ToDoItem = require('../models/GPT')
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
router.get('/simonApp/',
  isLoggedIn,
  async (req, res, next) => {
      const show = req.query.show
    items = 
        await ToDoItem.find({userId:req.user._id})
            res.render('simonApp',{items});
});


/* add the value in the body to the list associated to the key */
router.post('/simonApp',
  isLoggedIn,
  async (req, res, next) => {
      const prompt = req.body.userInput;
      const response = await openai.createCompletion({
        model: "text-davinci-003",
        prompt,
      });
      const request = new ToDoItem(
        {input:req.body.userInput,
         output: response.data.choices[0].text,
         createdAt: new Date(),
         userId: req.user._id
        })
      await request.save();
      res.redirect('/simonApp')
});

router.get('/simonApp/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /simonApp/remove/:itemId")
      await simonAppItem.deleteOne({_id:req.params.itemId});
      res.redirect('/simonApp')
});

router.get('/simonApp/complete/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /simonApp/complete/:itemId")
      await ToDoItem.findOneAndUpdate(
        {_id:req.params.itemId},
        {$set: {completed:true}} );
      res.redirect('/simonApp')
});

router.get('/simonApp/uncomplete/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /simonApp/complete/:itemId")
      await ToDoItem.findOneAndUpdate(
        {_id:req.params.itemId},
        {$set: {completed:false}} );
      res.redirect('/simonApp')
});

router.get('/simonApp/edit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /simonApp/edit/:itemId")
      const item = 
       await ToDoItem.findById(req.params.itemId);
      //res.render('edit', { item });
      res.locals.item = item
      res.render('edit')
      //res.json(item)
});

router.post('/simonApp/updateTodoItem',
  isLoggedIn,
  async (req, res, next) => {
      const {itemId,item,priority} = req.body;
      console.log("inside /simonApp/complete/:itemId");
      await ToDoItem.findOneAndUpdate(
        {_id:itemId},
        {$set: {item,priority}} );
      res.redirect('/simonApp')
});

router.get('/simonApp/byUser',
  isLoggedIn,
  async (req, res, next) => {
      let results =
            await ToDoItem.aggregate(
                [ 
                  {$group:{
                    _id:'$userId',
                    total:{$count:{}}
                    }},
                  {$sort:{total:-1}},              
                ])
        // if you comment out lines 125-128 you can see the raw data      
        results = 
           await User.populate(results,
                   {path:'_id',
                   select:['username','age']})

        //res.json(results)
        res.render('summarizeByUser',{results})
});



module.exports = router;