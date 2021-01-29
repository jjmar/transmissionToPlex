#!/bin/bash

export TARGET_MOVIES_DIR="/absolute/path/to/plex/movies/library"
export TARGET_TV_DIR="/absolute/path/to/plex/movies/library"
export RPC_HOST="localhost"
export RPC_PORT="9000"
export RPC_USER="deluge"
export RPC_PASS="deluge"

python3 /home/pi/Plex/transmissionToPlex/transmission_to_plex/main.py
