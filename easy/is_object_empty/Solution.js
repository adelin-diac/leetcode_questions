/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function (obj) {
  if (Array.isArray(obj)) {
    return obj.length === 0;
  }
  for (let _ in obj) {
    return false;
  }
  return true;
};

// or
var isEmptyO_N_time = function (obj) {
  if (Object.keys(obj).length === 0) {
    return true;
  }

  return false;
};

console.log(isEmpty({ x: 5, y: 42 }));
console.log(isEmpty({}));
console.log(isEmpty([null, false, 0]));
console.log(isEmpty([]));
