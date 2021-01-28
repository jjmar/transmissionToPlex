from transmission_rpc import Client
from transmission_to_plex import classifier


def run():
    print('Hello')
    client = Client(host='localhost', port=9000)
    completed_torrents = [t for t in client.get_torrents() if t.progress == 100.0]

    for torrent in completed_torrents:
        type_of_torrent = classifier.classify_downloaded_content(torrent.files())
        move_files_to_plex_folder(client, torrent, type_of_torrent)
        client.remove_torrent([torrent.id])


def move_files_to_plex_folder(client, torrent, type):
    TV_SHOW_DIR = '/Users/justin/Desktop/plex/target/tv'
    MOVIE_DIR = '/Users/justin/Desktop/plex/target/movie'
    target_directory = TV_SHOW_DIR if type == 'tv' else MOVIE_DIR

    client.move_torrent_data([torrent.id], target_directory)