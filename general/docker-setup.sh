#!/usr/bin/env bash
# check OS version cat /etc/os-release

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ${USER}

sudo su - ${USER}
pip3 install docker-compose
