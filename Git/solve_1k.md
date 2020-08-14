# VS CODE Git 1k 없애는 방법

Visual Studio Code (VS Code)를 사용하다보면 1k (혹은 5k 등) changes 문제가 발생하곤 한다. 기본적으로, 이 문제는 파일이나 폴더 등이 많은 디렉토리 (주로 Desktop) 등에 실수로 .git를 추가해서 생긴 문제이다.

우선은 git repository의 root 디렉토리가 어디인지를 찾아야 한다. 터미널에 다음 커멘드를 쳐보자.

```bash
git rev-parse --show-toplevel
```

이 명령어를 치면 내 root repository를 알 수 있다. 그렇다면 경로가 이런식으로 뜰 것이다.

```bash
/Users/keepnode
```

그럼 이제 해당 경로로 이동해보자.

```bash
cd /Users/keepnode
```

거기서 해당 디렉토리에 어떤 파일들이 있는지 알아보자.

```bash
ls -a
```

이 디렉토리에 .git이 있을 것이다. 그러면 해당 디렉토리에서 이 명령어를 쳐보자.

```bash
rm -r -f .git
```

(-f는 force의 약자이다.)

이제 명령어가 실행 된 이후에 visual studio code를 동기화하면 말끔하게 5k가 사라진 것을 볼 수 있을 것이다.

p.s git clean -f -d 함부로 치지 마라. 강제로 삭제하는 명령어이기 때문에 복구하기 힘들 수 있다. 정 궁금하면 git clean -d -n 을 쳐봐라. clean이 어떻게 되는지 미리 볼 수 있는 코드이다.
