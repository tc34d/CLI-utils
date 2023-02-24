#!/bin/bash
#network
echo would you like to connect to the wifi y/n
read bean
if bean == "y" then;
sudo pacman -S network-manager
sudo iwconfig wlan0 up
nmcli radio wifi on
nmcli radio wifi
sudo iw wlan0 scan | grep SSID
read input
sudo nmcli --ask dev wifi connect $input 
else
echo continuing through ethernet
fi

# installing common packages
if sudo pacman -Qi neofetch vi vim  > /dev/null ;then
    echo "packages already installed continueing with script"
else
 yes | sudo pacman -S neofetch vi vim 

fi

if sudo pacman -Qi firefox libreoffice > /dev/null ;then
    echo "would you like to install firefox and libreoffice y/n"
    read option
    if [ $option=="y" ]; then
        sudo pacman -S firefox libreoffice
    else
        echo "skipping install of firefox and libreoffice"
    fi
fi
sudo pacman -Syyu
echo "step finnished"
echo -e
echo "type in any other packages that you want to install"
read packages
sudo pacman -S $packages