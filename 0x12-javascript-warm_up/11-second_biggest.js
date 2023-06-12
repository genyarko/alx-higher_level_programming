#!/usr/bin/node

function findSecondBiggest(numbers) {
  if (numbers.length <= 1) {
    return 0;
  }

  let biggest = -Infinity;
  let secondBiggest = -Infinity;

  for (let i = 0; i < numbers.length; i++) {
    const num = parseInt(numbers[i]);

    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest && num < biggest) {
      secondBiggest = num;
    }
  }

  return secondBiggest;
}

const args = process.argv.slice(2);
console.log(findSecondBiggest(args));
