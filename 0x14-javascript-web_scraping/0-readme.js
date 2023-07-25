#!/usr/bin/node

const fs = require('fs');

// Get the file path and content from command line arguments
const filePath = process.argv[2];
const fileContent = process.argv[3];

// Write the file content to the specified file path
fs.writeFile(filePath, fileContent, (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`File ${filePath} written successfully.`);
  }
});

