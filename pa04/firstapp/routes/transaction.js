const express = require('express');
const router = express.Router();
const Transaction = require('../models/transactionItems');
const User = require('../models/User')

// /* **************************************** */

isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
  }

  router.get('/transaction/',
  isLoggedIn,
  async (req, res, next) => {
      const show = req.query.show
      const completed = show=='completed'
      let items=[]
      if (show) { // show is completed or todo, so just show some items
        items = 
          await ToDoItem.find({userId:req.user._id, completed})
                        .sort({completed:1,priority:1,createdAt:1})
      }else {  // show is null, so show all of the items
        items = 
          await ToDoItem.find({userId:req.user._id})
                        .sort({completed:1,priority:1,createdAt:1})

      }
            res.render('toDoList',{items,show,completed});
});



/* add the value in the body to the list associated to the key */
router.post('/transaction',
  isLoggedIn,
  async (req, res, next) => {
      const todo = new ToDoItem(
        {item:req.body.item,
         createdAt: new Date(),
         completed: false,
         priority: parseInt(req.body.priority),
         userId: req.user._id
        })
      await todo.save();
      res.redirect('/transaction')
});
