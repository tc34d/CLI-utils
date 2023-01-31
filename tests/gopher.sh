#!/bin/bash
os==cat /etc/os-release | grep name
if $os == "Arch Linux"; then
    sudo pacman -Syu lynx
elif $os == "Fedora"; then
    dnf install lynx
elif $os == "Debian GNU/Linux"; then
    sudo apt-get install lynx

lynx gopher://gopher.floodgap.com