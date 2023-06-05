#!/bin/bash

build () {
    pip install -r requirements.txt
    return 
}


main () {
    echo "
Choose an action you want:
1) build
0) exit
    "

    read -p "Enter selection [number] > "
    if [[ $REPLY =~ ^[0-9]+$ ]]; then
        if [[ $REPLY == 0 ]]; then
            echo "Program terminated."
            exit
        fi
        if [[ $REPLY == 1 ]]; then
            echo "pip install -r requirements.txt"
            # pip install -r requirements.txt
            exit
        fi
    else
        echo "Invalid entry." >&2
        exit 1
    fi
}

main
