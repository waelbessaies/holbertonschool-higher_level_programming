#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const Array = process.argv.sort();
  console.log(Array.reverse()[1]);
}
