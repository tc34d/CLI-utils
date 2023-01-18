#!/bin/bash

# Scan for available wireless networks
sudo iw wlan0 scan | grep SSID

echo -n "Enter the SSID of the network you want to connect to: "
read ssid

# Connect to the wireless network
sudo iw wlan0 connect "$ssid"

# Get the gateway IP from the DHCP server
echo dhcpd wlan0 | grep 'router'

# Set the network as the default route
ip route add default via "$gateway" dev wlan0

# Check if the connection was successful by pinging a website
if ping -c 1 google.com; then
  echo "Successfully connected to the internet!"
else
  echo "Failed to connect to the internet. Please check your network settings."
fi
