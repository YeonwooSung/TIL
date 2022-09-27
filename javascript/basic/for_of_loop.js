// 기존 for과 for in의 문제점을 보완한 for of 문법
// for of는 iterable한 객체에 대해서만 사용 가능하다.
// iterable한 객체란 Symbol.iterator 메소드를 가지고 있는 객체를 말한다.
// Symbol.iterator 메소드는 next 메소드를 가지고 있는 객체를 반환한다.
// next 메소드는 value와 done 속성을 가지고 있는 객체를 반환한다.
// value는 현재 반복되고 있는 값이고, done은 반복이 끝났는지를 나타낸다.
// done이 true이면 반복이 끝난 것이고, false이면 반복이 끝나지 않은 것이다.

let arr = [1, 2, 3, 4, 5];
for (let value of arr) {
    console.log(value);
}

for (let value of 'Hello') {
    console.log(value);
}
