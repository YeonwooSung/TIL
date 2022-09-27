// Spread operator를 사용하면 배열을 펼칠 수 있다.

const arr = [1, 2, 3, 4, 5];
console.log(...arr); // 1 2 3 4 5

function test(a, b) {
    return a + b;
}
const data = [1, 2];
console.log(test(...data)); // 3


// Rest parameter를 사용하면 배열을 합칠 수 있다.

function test2(...data) {
    return data;
}
console.log(test2(1, 2, 3, 4, 5)); // [1, 2, 3, 4, 5]

function test3(a, b, ...data) {
    return data;
}
console.log(test3(1, 2, 3, 4, 5)); // [3, 4, 5]
