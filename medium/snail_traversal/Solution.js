/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function (rowsCount, colsCount) {
  const temp = new Array();
  if (rowsCount * colsCount !== this.length) {
    return [];
  }
  for (let i = 0; i < this.length; i++) {
    let row = i % rowsCount;
    let col = Math.floor(i / rowsCount);
    if (col % 2 === 1) {
      row = rowsCount - 1 - row;
    }
    if (i < rowsCount) {
      temp[row] = new Array();
    }
    temp[row][col] = this[i];
  }
  return temp;
};

let arr = [1, 2, 3, 4];
console.log(arr.snail(1, 4)); // [[1,2,3,4]]

arr = [19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15];
console.log(arr.snail(5, 4));

arr = [1, 2];
console.log(arr.snail(2, 2));
