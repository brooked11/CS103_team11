/////////////////////////////////////////////////////////////////////////////

const express = require('express');
const router = express.Router();
const TransactionItems = require('../models/TransactionItems');
const User = require('../models/User');

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
    let items= await TransactionItems.find({userId:req.user._id});
    res.render('transaction',{items});
  }
);


/* add the value in the body to the list associated to the key */
// router.post('/transaction',
//   isLoggedIn,
//   async (req, res, next) => {
//       const transaction = new TransactionItems(
//         {description:req.body.description,
//           amount: req.body.amount,
//           category: req.body.category,
//           date: req.body.date,
//          userId: req.user._id
//         })
//       await transaction.save();
//       res.redirect('/transaction')
// });

// router.get('/todo/remove/:itemId',
//   isLoggedIn,
//   async (req, res, next) => {
//       console.log("inside /todo/remove/:itemId")
//       await ToDoItem.deleteOne({_id:req.params.itemId});
//       res.redirect('/toDo')
// });

// router.get('/todo/edit/:itemId',
//   isLoggedIn,
//   async (req, res, next) => {
//       console.log("inside /todo/edit/:itemId")
//       const item = 
//        await ToDoItem.findById(req.params.itemId);
//       //res.render('edit', { item });
//       res.locals.item = item
//       res.render('edit')
//       //res.json(item)
// });

// router.post('/transaction/updateTransactionItem',
//   isLoggedIn,
//   async (req, res, next) => {
//       const {itemId,item,priority} = req.body;
//       console.log("inside /todo/complete/:itemId");
//       await ToDoItem.findOneAndUpdate(
//         {_id:itemId},
//         {$set: {item,priority}} );
//       res.redirect('/transaction')
// });

module.exports = router;