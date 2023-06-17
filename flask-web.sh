#!/bin/bash

# Execution exits when an error is encountered
set -e

check_dir_exists() {
    dir_name=$1
    if [[ -d $dir_name ]]; then
        # cd $dir_name
        # empty statement
        :
    else
        echo "no such directory: '$dir_name'" >&2
        exit 1
    fi

    return 0
}

check_command_exists() {
    local ret='0'
    command -v $1 >/dev/null 2>&1 || { local ret='1'; }

    # fail on non-zero return value
    if [ "$ret" -ne 0 ]; then
        echo "no such command: '$1'" >&2
        exit 1
    fi

    return 0
}

activate_venv() {
    if source venv/bin/activate; then
        # pip install -r requirements.txt
        # empty statement
        :
    else
        echo "Cannot: activate virtual environment" >&2
        exit 1
    fi
}

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

init () {
    activate_venv
    check_command_exists flask

    # Initialize the migration database environment
    flask db init
    check_dir_exists migrations
    flask db migrate -m "init"

}

update() {
    activate_venv
    check_command_exists flask
    check_dir_exists migrations

    # Execute the migration script
    flask db upgrade
}

run () {
    activate_venv
    check_command_exists flask
    python -m flask run --debug
}

main () {
    echo "
    Choose an action you want:
    1) run
    2) build
    3) init
    4) update
    0) exit
    "

    read -p "Enter selection [number]: "
    case $REPLY in
        1)
            run
            exit 0
            ;;
        2)
            build
            exit 0
            ;;
        3)
            init
            exit 0
            ;;
        4)
            update
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
