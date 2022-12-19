#!/bin/bash

# Check if the required command-line arguments were provided
if [ "$#" -ne 2 ]; then
  echo "Usage: connect WIFI_SSID WIFI_PASSWORD"
  exit 1
fi

# Store the SSID and password in variables
ssid=$1
password=$2

# Connect to the WiFi network
nmcli device wifi connect "$ssid" password "$password"
