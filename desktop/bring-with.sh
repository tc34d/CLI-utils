#!/bin/bash

read -p "Would you like to move the .cpp files into the /usr/bin directory? [y/n]: " move_cpp
if [[ $move_cpp == "y" ]]; then
    gcc -o calc calc.cpp
    gcc -o flmaker flmaker.cpp
    gcc -o pswgen pswgen.cpp
    sudo mv calc flmaker pswgen /usr/bin/
fi

read -p "Would you like to move the gopher program into the /usr/bin directory? [y/n]: " move_gopher
if [[ $move_gopher == "y" ]]; then
    cd ../network
    cp gopher.sh gopher
    chmod +x gopher
    sudo mv gopher /usr/bin/
fi
