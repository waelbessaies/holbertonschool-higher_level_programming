#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let j = 0;
  for (let i = 0; list.length > i; i++) {
    if (list[i] === searchElement) {
      j++;
    }
  }
  return j;
};
