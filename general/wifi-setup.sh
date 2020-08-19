#!/usr/bin/env bash
# NOTES
# 1. wifi setup
# 1.1 ssh to raspberry pi
# 1.2 Open the wpa-supplicant configuration file in vim
# 1.3 Add
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
