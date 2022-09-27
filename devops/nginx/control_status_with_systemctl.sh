#!/bin/bash

# nginx 설치
sudo apt update 
sudo apt install nginx

# 방화벽 설정하기
sudo ufw app list
sudo ufw allow 'Nginx HTTP'
sudo ufw status

# systemctl로 nginx 컨트롤하기
sudo systemctl start nginx     # nginx 시작
sudo systemctl stop nginx      # nginx 멈추기
sudo systemctl restart nginx   # nginx 재시작(멈추고 다시 시작)
sudo systemctl reload nginx    # 설정 파일만 수정했을 경우 연결을 끊지 않고 수정사항 적용시키기
sudo systemctl disable nginx   # nginx는 서버가 부팅되면 자동으로 시작된다. 이 설정을 지우기
sudo systemctl enable nginx    # 위의 설정을 다시 enable 시키기

# nginx의 상태 확인
sudo systemctl status nginx
