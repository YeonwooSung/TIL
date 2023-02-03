# D-Bus

D-Bus란 Red Hat 진영에서 만든 IPC(Inter-Process Communication)의 일종으로, 리눅스에서 동시적으로 실행되는 여러 프로세스들끼리 통신을 하기 위한 방식이다.
D-Bus는 CORBA 등을 대체하기 위해 만들어졌다.

D-Bus는 system daemon과 per-user-login-session daemon 이렇게 두개의 데몬 프로세스를 제공한다:

    - system daemon은 새로운 장치 연결 이벤트나 프린터 큐의 변경사항 확인 등의 시스템 및 로우레벨 적인 IPC 및 이벤트 관리를 위한 미들웨어이다.
    - per-user-login-session daemon은 사용자 어플리케이션들 사이의 IPC를 위한 기능들을 제공한다.

## 예제

[simple_dbus.py](./simple_dbus.py)는 dbus python binding API를 사용해서 systemd에 명령을 내리는 간단한 예제이다.
