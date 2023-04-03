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

  