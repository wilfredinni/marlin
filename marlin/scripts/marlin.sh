#!/bin/sh

marlin() {
    bookmark_name=$1

    if [ ! -d "$HOME/.marlin" ]; then
        mkdir "$HOME/.marlin"
    fi

    if [ -z "$bookmark_name" ]; then
        marlin_help
        exit 0
    fi

    if [ -f "$HOME/.marlin/$bookmark_name" ]; then
        bname=$(cat "$HOME/.marlin/$bookmark_name")
        cd "$bname" || exit
    else
        echo "Bookmark does not exists: $bookmark_name"
    fi
}
