#!/usr/bin/node

const arg = process.argv[2];
const converted = parseInt(arg);

if (!isNaN(converted)) {
  console.log("My number: " + converted);
} else {
  console.log("Not a number");
}
