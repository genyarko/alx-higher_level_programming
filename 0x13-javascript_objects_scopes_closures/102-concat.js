#!/usr/bin/node

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading source file 1: ${err}`);
    return;
  }

  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading source file 2: ${err}`);
      return;
    }

    const concatenatedContent = data1 + data2;

    fs.writeFile(destinationFile, concatenatedContent, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to destination file: ${err}`);
        return;
      }

      console.log('Concatenation successful. Destination file created.');
    });
  });
});
