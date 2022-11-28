# git stash

작업을 하다가 임시 저장해야하는 상황이 있다.
커밋 메세지도 떠오르지 않고 그냥 잠깐 저장하고 다른 작업을 하고 싶을때 그렇다.
이러한 경우에 가장 좋은 대안이 바로 stash를 사용하는 것이다.

간단하게 말해서 stash를 사용하면 현재까지 작업하던 내용이 다른 곳에 임시로 저장이 되고, 변경 전으로 파일들이 되돌아간다.
추후에 다시 해당 내용을 로딩하고 싶다면 stash pop을 통해서 임시저장 내용을 꺼내면 된다.

```bash
# save as stash
$ git stash

# get list of stashes
$ git stash list

# get stash
$ git stash pop
```
