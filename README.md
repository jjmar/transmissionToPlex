# transmissionToPlex

Simple script which moves completed transmission movie/tv
show downloads into their respective plex library folders and then deletes the torrent.

### Configuration

Environment Variable | Function
------------ | -------------
RPC_HOST | Host for transmission RPC server
RPC_PORT | Port for transmission RPC server
RPC_USER | User for transmission RPC server
RPC_PASS | Password for transmission RPC server
TARGET_MOVIE_DIR | Folder to send completed movies
TARGET_TV_DIR | Folder to send completed tv shows

### Setup

1. Clone repo
2. Install requirements, `pip install -r requirements.txt`
3. Set transmission to use `on_transmission_complete.sh` upon torrent completion
4. Set your environment variables in `on_transmission_complete.sh`

Notes:
- Ensure `on_transmission_complete.sh` is executable
- Ensure script can be run by transmission
- Ensure transmission can move files to target directories. 