/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  let len = arr.length;
  let maxIdx = len - 1;
  for (let i = 0; i < maxIdx / 2; i++) {
    arr[i] = fn(arr[i], i);

    arr[maxIdx - i] = fn(arr[maxIdx - i], maxIdx - i);
  }
  if (len % 2) {
    let idx = (len - 1) / 2;
    console.log("idx", idx);
    arr[idx] = fn(arr[idx], idx);
  }

  return arr;
};

// or
var map = function (arr, fn) {
  let len = arr.length;
  for (let i = 0; i < len; i++) {
    arr[i] = fn(arr[i], i);
  }

  return arr;
};

const arr = [1, 2, 3];
const fn = function plusone(n) {
  return n + 1;
};
console.log(map(arr, fn));
