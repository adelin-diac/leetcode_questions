var TimeLimitedCache = function () {
  this.vals = {};
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  let ret = false;
  if (key in this.vals) {
    ret = true;
    clearTimeout(this.vals[key].timeoutID);
  }

  this.vals[key] = {
    val: value,
    expired: false,
    timeoutID: setTimeout(() => {
      this.vals[key].expired = true;
    }, duration),
  };

  return ret;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
  if (key in this.vals && !this.vals[key].expired) {
    return this.vals[key].val;
  }
  return -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
  return Object.values(this.vals).filter((item) => !item.expired).length;
};

function test1() {
  const timeLimitedCache = new TimeLimitedCache();
  console.log(timeLimitedCache.set(1, 42, 1000)); // false
  setTimeout(() => console.log(timeLimitedCache.get(1)), 1000); // -1
  console.log(timeLimitedCache.get(1)); // 42
  console.log(timeLimitedCache.count()); // 1
}

function test2() {
  const timeLimitedCache = new TimeLimitedCache(); // null
  console.log(timeLimitedCache.set(1, 42, 50)); // false
  setTimeout(() => console.log(timeLimitedCache.set(1, 50, 100)), 40); // true
  setTimeout(() => console.log(timeLimitedCache.get(1)), 50);
  setTimeout(() => console.log(timeLimitedCache.get(1)), 120);
  setTimeout(() => console.log(timeLimitedCache.get(1)), 200);
  setTimeout(() => console.log(timeLimitedCache.count()), 250);
}

test2();
