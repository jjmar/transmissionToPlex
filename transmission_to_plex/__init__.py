from transmission_to_plex.main import run

if __name__ == '__main__':
    run()


# Configuration
# Source dir (might not be needed)
# Target movie dir
# Target tv dir
# Transmission RPC Pass / User

# Tasks
# Get list of all torrents
    # Filter for only completed
# For each torrent (likely one),
    # Get list of files
    # Count number of movie files using mimetype
# For each torrent with <= 2 movie files
    # Use rpc to transfer torrent to movie folder
# For each torrent with > 2 movie files
    # Use rpc to transfer torrent to tv shows folder
# Delete each completed torrent

