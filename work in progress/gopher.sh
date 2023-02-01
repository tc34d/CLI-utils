#!/bin/bash
os=cat /etc/os-release | grep name

#the first if an elif statements check what distro is running 
#the nested if statements check if lynx is installed if ti is it runs the gopher thing

if $os == "Arch Linux"; then
    if sudo pacman -Qi lynx > /dev/null; then
        lynx gopher://gopher.floodgap.com
    fi
    sudo pacman -Syu lynx
    
elif $os == "Fedora"; then
    if sudo dnf list installed | grep lynx >/dev/null; then
        echo whatis
    fi;
    dnf install lynx
    
elif $os == "Debian GNU/Linux"; then

    sudo apt-get install lynx

fi
