#!/bin/bash
var=$=cat /etc/os-release | grep name

#the first if an elif statements check what distro is running 
#the nested if statements check if lynx is installed if ti is it runs the gopher thing

if $ '=' "Arch Linux"; then
    if sudo pacman -Qi lynx > /dev/null; then
        lynx gopher://gopher.floodgap.com
    fi
    sudo pacman -Syu lynx
    
elif $ '=' "Fedora"; then
    if sudo dnf list installed | grep lynx >/dev/null; then
        echo whatis
    fi
    dnf install lynx
    
elif $ '=' "Debian GNU/Linux"; then

    sudo apt-get install lynx

fi
lynx gopher://gopher.floodgap.com