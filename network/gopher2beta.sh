#!/bin/bash

if distro | grep Name == "Name: Arch Linux"; then
    if sudo pacman -Qi lynx > /dev/null; then
        lynx gopher://gopher.floodgap.com
    fi
    sudo pacman -Syu lynx
    
elif distro | grep Name == "Name: Fedora"; then
    if sudo dnf list installed | grep lynx >/dev/null; then
        echo whatis
    fi
    dnf install lynx
    
elif distro | grep Name "Name: Debian GNU/Linux"; then

    sudo apt-get install lynx

fi
lynx gopher://gopher.floodgap.com