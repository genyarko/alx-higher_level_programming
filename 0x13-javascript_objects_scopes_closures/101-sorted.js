#!/usr/bin/node

const { dict } = require('./101-data');

console.log('Initial dictionary:', dict);

const newDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (occurrence in newDict) {
    newDict[occurrence].push(userId);
  } else {
    newDict[occurrence] = [userId];
  }
}

console.log('New dictionary:', newDict);
