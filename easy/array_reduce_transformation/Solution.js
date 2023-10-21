var reduce = function (nums, fn, init) {
  val = init;
  for (let num of nums) {
    val = fn(val, num);
  }
  return val;
};

console.log(reduce([1, 2, 3, 4], (sum, curr) => sum + curr, 0));
console.log(reduce([1, 2, 3, 4], (sum, curr) => sum + curr * curr, 100));
