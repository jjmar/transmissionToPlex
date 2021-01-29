from transmission_rpc import Client

import classifier
import config


class Main:
    def __init__(self, config):
        self.config = config
        self.client = Client(host=config.rpc_host,
                             port=config.rpc_port,
                             username=config.rpc_user,
                             password=config.rpc_pass)

    def run(self):
        completed_torrents = [t for t in self.client.get_torrents() if t.progress == 100.0]

        for torrent in completed_torrents:
            type_of_torrent = classifier.classify_downloaded_content(torrent.files())
            self.move_files_to_plex_folder(torrent, type_of_torrent)
            self.client.remove_torrent([torrent.id])

    def move_files_to_plex_folder(self, torrent, type):
        target_directory = self.config.movies_dir if type == classifier.MediaType.MOVIE else self.config.tv_dir

        self.client.move_torrent_data([torrent.id], target_directory)


if __name__ == "__main__":
    config = config.Config()
    main = Main(config)
    main.run()


