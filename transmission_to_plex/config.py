import os


class Config:
    def __init__(self):
        self.rpc_host = os.environ.get('RPC_HOST')
        self.rpc_port = os.environ.get('RPC_PORT')
        self.rpc_user = os.environ.get('RPC_USER')
        self.rpc_pass = os.environ.get('RPC_PASS')
        self.movies_dir = os.environ.get('TARGET_MOVIE_DIR')
        self.tv_dir = os.environ.get('TARGET_TV_DIR')
