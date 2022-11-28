# patch with git

여러 개발자들끼리 협업을 하다보면 다양한 상황이 발생할 수 있는데, 이 중 대표적인 경우가 파일 변경사항을 효과적으로 관리하기 위해서 패치를 사용하는 경우이다.
이러한 경우, git patch를 사용해서 문제를 해결할 수 있다.

```bash
# 1) patch file 만들기
$ git diff {start commit id} {end commit id} > {patch.diff path}

# 2) patch diff file을 적용하기
$ patch -p1 < {patch.diff path}
```

patch 파일을 만들 때 캐시 옵션을 사용해서 commit 전에 패치 파일을 만들 수도 있다:

```bash
# staging
$ git add {changed_file}
# generate diff patch file
$ git diff --cached >> mypatch.diff

# apply patch
$ git apply mypatch.diff
```

패치 파일을 로컬 커밋으로 적용시키는 방법도 있다:

```bash
$ git am {patch file}
```

## 패치 파일 적용 시 unstaged 파일들에만 적용하는 방법

patch -p[number] < [patch file name] 명령어로 패치 파일을 적용하면, unstaged 영역에만 파일이 저장되며 commit으로 반영되진 않는다.
패치 내용을 조금 수정하고 commit을 반영하고 싶을 때 이런 방법을 사용할 수 있다.

```bash
# -p1는 file path의 첫번째 경로를 무시하고 패치를 적용한다는 의미
$ patch -p1 < patchfile

# -p0는 패치에 보이는 file path를 생략하지 않고 적용한다는 의미
$ patch -p0 < patchfile
```
