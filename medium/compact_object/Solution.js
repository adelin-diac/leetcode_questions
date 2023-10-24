/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function (obj) {
  let my_obj = {};
  if (Array.isArray(obj)) {
    my_obj = obj.filter(Boolean);
    my_obj = my_obj.map((item) => compactObject(item));
  } else if (obj instanceof Object) {
    for (let key in obj) {
      if (obj[key]) {
        my_obj[key] = compactObject(obj[key]);
      }
    }
  } else if (Boolean(obj)) {
    my_obj = obj;
  }
  return my_obj;
};

let obj = [null, 0, false, 1]; // [1]
console.log(compactObject(obj));
// compactObject(obj);

obj = { a: null, b: [false, 1] }; // {"b": 1}
console.log(compactObject(obj));
// compactObject(obj);

obj = [null, 0, 5, [0], [false, 16]];
console.log(compactObject(obj));
// compactObject(obj);
