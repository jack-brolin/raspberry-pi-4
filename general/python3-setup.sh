#!/usr/bin/env bash
# NOTES
# 1. Install python
# 1.1 Update the Raspbian
sudo apt-get update

# 1.2 Prerequisites
sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim

# 1.3 Download Python
wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz

# 1.4 Install Python 3.8
sudo tar zxf Python-3.8.0.tgz
cd Python-3.8.0
sudo ./configure --enable-optimizations
sudo make -j 4
sudo make altinstall

# 1.5 Make Python 3.8 as the default version
echo "alias python=/usr/local/bin/python3.8" >> ~/.bashrc
source ~/.bashrc

# 1.6 Clean up
sudo rm -rf Python-3.8.0.tgz
sudo rm -rf Python-3.8.0
