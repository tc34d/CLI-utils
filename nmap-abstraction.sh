#!/bin/bash

# Check if nmap is installed
if ! command -v nmap &> /dev/null
then
    echo "Error: nmap is not installed. Please install nmap and try again."
    exit 1
fi

# Prompt for target
read -p "Enter the hostname or IP address to scan: " target

# Prompt for port range
read -p "Enter the port range to scan (e.g. 1-1024): " port_range

# Scan target with nmap
nmap -p $port_range $@ $target

# Display results
echo "Open ports:"
nmap -p $port_range $@ $target | grep "open" | cut -d "/" -f 1
