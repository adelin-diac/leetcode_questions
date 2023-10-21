var compose = function (functions) {
  i = functions.length;

  return function (x) {
    val = x;
    for (i; i > 0; i--) {
      val = functions[i - 1](val);
    }
    return val;
  };
};

const fn = compose([(x) => x + 1, (x) => 2 * x]);
console.log(fn(4)); // 9
