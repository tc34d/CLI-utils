#!/bin/bash
# full setup script for ArchLinux
if sudo pacman -Qi neofetch vi vim  > /dev/null ;then
    echo packages already installed continueing with script
else
 yes | sudo pacman -S neofetch vi vim 

fi
if sudo pacman -Qi firefox libreoffice > /dev/null ;then
    echo would you like to install firefox and libreoffice y/n
    read option
    if [ $option=="y" ]; then
        sudo pacman -S firefox libreoffice
    else
        echo skipping install of firefox and libreoffice
    fi
fi