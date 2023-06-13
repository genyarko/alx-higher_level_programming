#!/usr/bin/node

const fs = require('fs');
const path = require('path');

function concatFiles(sourceFile1, sourceFile2, destinationFile) {
  const file1Content = fs.readFileSync(sourceFile1, 'utf8');
  const file2Content = fs.readFileSync(sourceFile2, 'utf8');

  const concatenatedContent = file1Content + file2Content;

  fs.writeFileSync(destinationFile, concatenatedContent, 'utf8');
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

concatFiles(sourceFile1, sourceFile2, destinationFile);
