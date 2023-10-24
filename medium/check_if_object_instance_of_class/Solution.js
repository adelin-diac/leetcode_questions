/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function (obj, classFunction) {
  // use default checks (if undefined or if `classFunction` is not a function)
  if (obj === null || obj == undefined || typeof classFunction !== "function") {
    return false;
  }

  let currPrototype = Object.getPrototypeOf(obj);

  while (currPrototype !== null) {
    if (currPrototype === classFunction.prototype) {
      return true;
    }
    currPrototype = Object.getPrototypeOf(currPrototype);
  }
  return false;
};

class Animal {}
class Dog extends Animal {}
console.log(checkIfInstanceOf(new Dog(), Animal));
console.log(checkIfInstanceOf(new Date(), Date));
console.log(checkIfInstanceOf(5, Number));
function Container(value) {
  this.value = value;
}
function Box(value) {
  this.value = value;
}
const b = new Box(1);
console.log(checkIfInstanceOf(b, Container));
