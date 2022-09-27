#!/bin/bash

# 의존 패키지 설치
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools

# 가상환경 설정하고 접속하기
sudo apt install python3-venv
python3 -m venv venv-name
source venv-name/bin/activate

# gunicon 설치
pip install wheel # package에 wheel archive가 없어도 설치되게끔 하기 위해서라는데 일단 설치한다. 
pip install gunicorn flask
which gunicorn  #gunicorn 경로 확인하기

# service 파일 만들기 (venv에서 나오고 작업을 해야 함)
# nano 대신 vim을 써도 됨
sudo nano /etc/systemd/system/myproject.service

# service 파일 내용 예시
#
# [Unit]
# Description=Gunicorn instance to serve myproject
# After=network.target

# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/myproject
# Environment="PATH=/home/ubuntu/myproject/venv-name/bin"
# ExecStart=/home/ubuntu/myproject/venv-name/bin/gunicorn --workers 1 --bind unix:myproject.sock -m 007 wsgi:app

# [Install]
# WantedBy=multi-user.target

# 추가로, 위의 --workers 1은 1개의 worker를 사용한다는 뜻이고, --bind unix:myproject.sock은 unix socket을 사용한다는 뜻이다.


# service 파일 저장하고 실행하기
sudo systemctl start myproject
sudo systemctl enable myproject

# service 파일의 상태 확인하기
sudo systemctl status myproject
