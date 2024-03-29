# Today I Learned

## Python

* [4 for loop tricks](./python/4_for_loop_tricks.py)
* [Concurrent programming in Python](./python/concurrency/)
        - [asyncio loop](./python/concurrency/async_loop.py)
        - [http session with asyncio](./python/concurrency/asyncio_http_example.py)
        - [multi-threaded token bucket example](./python/concurrency/simple_token_bucket.py)
        - [multi-threaded queue](./python/concurrency/simple_queue.py)
* [Decorators](./python/decorator/)
        - [Custom decorator for private method](./python/decorator/private.py)
* [Empty Trash bin with Python code](./python/empty_trash_bin.py)
* [Generator](./python/generator/)
* [one liner codes](./python/one_liner.py)
* [Object Oriented Programming](./python/oop/)
* [Regular Expression with python - Simple example](./python/regex/simple_regex.py)
* [smooth 10 python tricks](./python/smooth_10_tricks.py)
* [Useful helper functions](./python/useful_helper_functions.py)

For more topics visit [here](./python/)

### PyTorch

* [PyTorch Hooks](./python/pytorch/pytorch_hooks/pytorch_hooks.py)
* [Patch an arbitrary function](./python/pytorch/torch_patch.py)

#### PyTorch Lightning

* [GAN - PyTorch Lightning implementation](./python/pytorch/pytorch_lightning/gan/gan.py)
* [Unit testing the PyTorch code](./python/pytorch/testing/how_to_test_if_pytorch_code_is_working_as_intended.md)

### setuptools

라이센스 등 classifier 부분에 태그를 추가할 때에는 내용을 정확히 작성하지 않으면 빌드 시에 오류가 발생한다.

* [참고 자료](https://pypi.org/classifiers/)
* [배포 관련](https://rampart81.github.io/post/python_package_publish/)
* [패키징 방법](https://data-newbie.tistory.com/770)

## Shell

* [Bash Function for returning string](./bash/function_return_string.sh)
* [Send multipart/form-data with curl](./bash/curl_multipart.sh)
* [Make own service with systemctl - Ubuntu](./bash/make_my_own_service.sh)
* [kill chrome in bash](./bash/kill_chrome.sh)
* [kill node js in bash](./bash/kill_node_js.sh)
* [Open Chromium with kiosk mode](./bash/chromium_kiosk_mode.sh)
* [Linux kernel version checking](./bash/linux_kern_ver_check.sh)
* [Ubuntu version checking](./bash/ubuntu_version_check.sh)

### Date

* [Unix timestamp](./bash/unix_timestamp.sh)

Below is a table that includes all commands for all datetime formats:

```
        Format/result           |       Command              |          Output
--------------------------------+----------------------------+------------------------------
YYYY-MM-DD                      | date -I                    | $(date -I)
YYYY-MM-DD_hh:mm:ss             | date +%F_%T                | $(date +%F_%T)
YYYYMMDD_hhmmss                 | date +%Y%m%d_%H%M%S        | $(date +%Y%m%d_%H%M%S)
YYYYMMDD_hhmmss (UTC version)   | date --utc +%Y%m%d_%H%M%SZ | $(date --utc +%Y%m%d_%H%M%SZ)
YYYYMMDD_hhmmss (with local TZ) | date +%Y%m%d_%H%M%S%Z      | $(date +%Y%m%d_%H%M%S%Z)
YYYYMMSShhmmss                  | date +%Y%m%d%H%M%S         | $(date +%Y%m%d%H%M%S)
YYYYMMSShhmmssnnnnnnnnn         | date +%Y%m%d%H%M%S%N       | $(date +%Y%m%d%H%M%S%N)
YYMMDD_hhmmss                   | date +%y%m%d_%H%M%S        | $(date +%y%m%d_%H%M%S)
Seconds since UNIX epoch:       | date +%s                   | $(date +%s)
Nanoseconds only:               | date +%N                   | $(date +%N)
Nanoseconds since UNIX epoch:   | date +%s%N                 | $(date +%s%N)
ISO8601 UTC timestamp           | date --utc +%FT%TZ         | $(date --utc +%FT%TZ)
ISO8601 UTC timestamp + ms      | date --utc +%FT%T.%3NZ     | $(date --utc +%FT%T.%3NZ)
ISO8601 Local TZ timestamp      | date +%FT%T%Z              | $(date +%FT%T%Z)
YYYY-MM-DD (Short day)          | date +%F\(%a\)             | $(date +%F\(%a\))
YYYY-MM-DD (Long day)           | date +%F\(%A\)             | $(date +%F\(%A\))
```

### brew

```bash
# uninstall git
$ brew uninstall git

# uninstall dbeaver-community by using --cask flag
$ brew uninstall --cask dbeaver-community

# use autoremove
$ brew autoremove

# use cleanup
$ brew cleanup
```

## Git

* [git 기본 사용 방법들](./Git/basic.md)
* [1k changes 문제 해결하기](./Git/solve_1k.md)
* [patch 생성 및 적용 방법](./Git/patch.md)
* [temporary saving with stash](./Git/stash.md)

## Javascript

* [Audio permission issue](./javascript/audio_permission_for_autoplay/README.md)
* [DOM class list](./javascript/DOM_classList/DOM_classList.md)
* [For of loop](./javascript/basic/for_of_loop.js)
* [Markdown parsing](./javascript/markdown_parsing/README.md)
* [PM2 commands](./javascript/pm2/pm2_commands.md)
* [Prevent SQL Injection in Node.js by using placeholders](./javascript/sql/prevent_sql_injection.js)
* [Promise](./javascript/basic/promise.js)
* [Spread operator & Rest operator have been added since ES6](./javascript/basic/spread_rest.js)

## Debugging

* [스마트폰 앱 브라우저에서 크롬 개발자 도구 사용하기](https://medium.com/cashwalk/%EC%8A%A4%EB%A7%88%ED%8A%B8%ED%8F%B0-%EC%95%B1-%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%97%90%EC%84%9C-%ED%81%AC%EB%A1%AC-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%8F%84%EA%B5%AC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-c6a34d9aeb02)

## Linux

### Add bookmark

Use simply Ctrl+D when you are in the desired directory.

* [Refernce](https://askubuntu.com/questions/83118/create-a-link-to-a-folder-on-the-left-panel-of-nautilus-file-manager)

## DevOps

* [Deploy flask with gunicorn](./devops/flask/deploy_with_gunicon.sh)
* [Setup NginX with systemctl](./devops/nginx/setup_nginx_with_systemctl.sh)
