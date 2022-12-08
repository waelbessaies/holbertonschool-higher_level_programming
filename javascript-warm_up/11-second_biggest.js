#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const Array = process.argv.slice(2);
  Array.sort((a, b) => b - a);
  console.log(Array[1]);
}
