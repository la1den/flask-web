#!/bin/bash

build () {
    echo "Starting build..."
    dir_name=venv
    python -m venv $dir_name
    if [[ -d $dir_name ]]; then
        if source venv/bin/activate; then
            pip install -r requirements.txt
        else
            echo "activate virtual environment '$dir_name'" >&2
            exit 1
        fi
    else
        echo "no such directory: '$dir_name'" >&2
        exit 1
    fi
    return 
}


main () {
    echo "
    Choose an action you want:
    1) build
    2) run
    0) exit
    "

    read -p "Enter selection [number]: "
    case $REPLY in
        1)
            build
            exit 0
            ;;
        2)
            source venv/bin/activate
            python -m flask run --debug
            exit 0
            ;;
        0)
            echo "Program terminated."
            exit 1
            ;;
        *)
            echo "Invalid entry." >&2
            exit 1
            ;;
    esac
}

main
