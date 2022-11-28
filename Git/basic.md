# Basic knowledges of using git for development

## Init

```bash
# initialise git repo
$ git init

# clone existing git repo
$ git clone <URL_OF_REPO_TO_CLONE>
```

## staging

```bash
# add all files in current directory to staged mode
$ git add .

# add test.txt to the stage
$ git add test.txt
```

### Make staged file to untracked

By using "git reset" command, you could make the staged file to untracked.

```bash
# git add를 통해 stage된 bbb.java 파일을 untracked로 다시 변경
$ git reset HEAD -- bbb.java
```

[reference link](https://codechacha.com/ko/git-remove-files-from-staging-area/)

## Commit

```bash
# commit with message
$ git commit -m "commit message"

# do staging and commiting at once - this only works for already tracked files (cannot use for new file)
$ git commit -am "stage and commit at once - only works for tracked files"

# add modifications to last commit
$ git commit --amend
```

### Commit specific lines of codes in chagned files

보통 변경된 파일을 스태이징한 뒤 이것을 커밋하기 때문에 커밋은 파일단위로 묶이게 된다. 의미있는 커밋 메세지를 유지하려다보면, 파일의 라인 단위로 변경사항을 묶고 싶을 경우가 있다. 지금까지 이런 식의 커밋을 위해 변경된 내용을 복사 붙여넣기 했다면 아래 방식도 사용해 보길 바란다.

```bash
$ git add -p
```

변경된 코드가 연속으로 있을경우 깃은 스스로 코드를 분할할 수 없다. 이러한 경우에는 e(edit)를 입력하고 편집 모드로 들어가 직접 스테이징할 라인을 선별할 수 있다.
이렇게 선택적으로 스태이징한 뒤 커밋하면 훨씬 의미있는 커밋을 만들 수 있다.

이제 이걸 커밋으로 생성해야하는데 커밋에 -v(verbose) 옵션을 주면 스태이징된 부분을 자세히 볼 수 있다.

```bash
$ git commit -v
```

## Log

```bash
# print out logs
$ git log

# show all diffs in the last commit
$ git show

# show all diffs in the specific commit
$ git show 289bd6a304b05cd11bafaf5416570b41ff96cf1c
```

For better UI, use the command below:

```bash
$ git log --graph
```

## Branch

```bash
# show current branch
$ git branch

# generate new branch - from existing branch
# the command below generates feature branch from master branch
$ git branch feature master

# change to feature branch
$ git checkout feature

# generate and change to feature branch
$ git checkout -b feature
```
