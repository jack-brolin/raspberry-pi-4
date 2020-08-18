# 1. Setup wifi
# 1.1 ssh to raspberry pi
# 1.2 Open the wpa-supplicant configuration file in vim
# 1.3 ADD
# ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
# update_config=1
# country=<Insert 2 letter ISO 3166-1 country code here>
#
# network={
#     ssid="<your-ssid>"
#     psk="<wifi-pass>"
# }
scp ./wifi.txt pi@raspberrypi.local://path/to/home/folder
sudo cat ~/wifi.txt | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf

# 2. Install python
# Move to home folder
# 2.1 Update the Raspbian
sudo apt-get update

# 2.2 Prerequisites
sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim

# 2.3 Download Python
wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz

# 2.4 Install Python 3.8
sudo tar zxf Python-3.8.0.tgz
cd Python-3.8.0
sudo ./configure --enable-optimizations
sudo make -j 4
sudo make altinstall

# 2.5 Make Python 3.8 as the default version
echo "alias python=/usr/local/bin/python3.8" >> ~/.bashrc
source ~/.bashrc

# 2.6 Clean up
sudo rm -rf Python-3.8.0.tgz
sudo rm -rf Python-3.8.0
