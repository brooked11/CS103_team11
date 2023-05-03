
'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var BrookeGPTSchema = Schema( {
  input: String,
  output: String,
  createdAt: Date,
  userId: {type:ObjectId, ref:'user' }
} );

module.exports = mongoose.model( 'BrookeGPT', BrookeGPTSchema );