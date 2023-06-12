#!/usr/bin/node

const arg = process.argv[2];
const size = parseInt(arg);

if (!isNaN(size)) {
  if (size <= 0) {
    console.log("Size must be a positive integer");
  } else {
    const row = "X".repeat(size);

    for (let i = 0; i < size; i++) {
      console.log(row);
    }
  }
} else {
  console.log("Missing size");
}
