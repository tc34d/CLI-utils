#!/bin/bash
sudo iwconfig wlan0 up
nmcli radio wifi on
nmcli radio wifi
sudo iw wlan0 scan | grep SSID
read input
sudo nmcli --ask dev wifi connect $input 
