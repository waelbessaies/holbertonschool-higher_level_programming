#!/usr/bin/node
exports.esrever = function (list) {
  const newls = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newls.push(list[i]);
  }
  return newls;
};
