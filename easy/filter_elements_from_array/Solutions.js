/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
  const newArr = [];
  arr.forEach((item, idx) => {
    if (fn(item, idx)) {
      newArr.push(item);
    }
  });
  return newArr;
};

let arr = [0, 10, 20, 30];
let fn = function greaterThan10(n) {
  return n > 10;
};
console.log(filter(arr, fn));

arr = [1, 2, 3];
fn = function firstIndex(n, i) {
  return i === 0;
};
console.log(filter(arr, fn));

arr = [-2, -1, 0, 1, 2];
fn = function plusOne(n) {
  return n + 1;
};
console.log(filter(arr, fn));
