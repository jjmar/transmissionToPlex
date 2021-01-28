#!/bin/bash

export TARGET_MOVIES_DIR="/Users/justin/Desktop/plex/target/movie"
export TARGET_TV_DIR="/Users/justin/Desktop/plex/target/tv"
export RPC_HOST="localhost"
export RPC_PORT="9000"
export RPC_USER="deluge"
export RPC_PASS="deluge"

source venv/bin/activate
python transmission_to_plex/main.py