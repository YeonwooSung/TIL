// Promise는 비동기 처리를 위한 객체이다.
// Promise는 비동기 처리가 끝나면 성공(resolve)하거나 실패(reject)한다.
// Promise는 성공(resolve)하면 then()을 호출하고, 실패(reject)하면 catch()를 호출한다.
// 특히 비동기 처리가 많이 일어나는 XMLHttpRequest 처리에서 주로 사용한다.

function get(url) {
    return new Promise((resolve, reject) => {
        const req = new XMLHttpRequest();
        req.open('GET', url);
        req.onload = () => req.status == 200 ? resolve(req.response) : reject(Error(req.statusText));
        req.onerror = (e) => reject(Error(`Network Error: ${e}`));
        req.send();
    });
}

get('https://api.github.com/users/kyungw00k').then((response) => {
    console.log('Success!', response);
}).catch((error) => {
    console.error('Failed!', error);
});
