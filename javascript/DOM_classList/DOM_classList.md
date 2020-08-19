# classList를 위한 메소드

## classList.add

선택한 element에 새로운 클래스를 추가하는 기능을 제공하는 메소드이다.

### example (classList.add)

```javascript
document.getElementById('test').classList.add('newClass');
```

위의 코드를 사용하면 새로운 클래스를 추가할 수 있다.

## classList.remove

선택한 element의 클래스 목록에서 매개변수로 주어진 클래스를 빼는 기능을 제공하는 메소드이다.

### example (classList.remove)

```javascript
document.getElementById('test').classList.remove('newClass');
```

위의 코드를 사용하면 test라는 id를 가진 요소의 클래스 목록에서 newClass라는 클래스를 제외시킬 수 있다.

## classList.toggle

선택한 element가 매개변수로 주어진 클래스값이 있는지 확인하고 없으면 더하고 있으면 제거한다. 이 메소드는 특정 클래스 값을 추가하고 제외하는 기능을 구현할 때 유용하다.

### example (classList.toggle)

```javascript
document.getElementById('test').classList.toggle('newClass');  // 추가
document.getElementById('test').classList.toggle('newClass');  // 제외
```

위의 예제에서, newClass를 매개변수롤 toggle() 메소드를 2번 호출했으니 newClass를 추가하였다가 다시 제외하게 된다.
