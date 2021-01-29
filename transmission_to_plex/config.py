import os


class Config:
    REQUIRED_ENV_VARS = ['RPC_HOST', 'RPC_PORT', 'TARGET_MOVIE_DIR', 'TARGET_TV_DIR']
    OPTIONAL_ENV_VARS = ['RPC_USER', 'RPC_PASS']

    def __init__(self):
        self.setup()
        self.validate()

    def setup(self):
        env_vars = self.REQUIRED_ENV_VARS + self.OPTIONAL_ENV_VARS

        for v in env_vars:
            setattr(self, v.lower(), os.environ.get(v))

    def validate(self):
        for v in self.REQUIRED_ENV_VARS:
            if getattr(self, v.lower()) is None:
                raise ValueError("{} is required to be set".format(v))

