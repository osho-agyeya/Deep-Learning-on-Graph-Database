from collections import defaultdict
from .environment import Environment

# There are too many layers and too many files to this config system


environment_box = Environment(None)

def set_environment(environment_name):
    environment_box.name = environment_name


def get(config_variable_name):
    # don't execute code in overrides till necessary
    from .overrides import overrides
    return overrides[environment_box.name][config_variable_name]


class Config(object):
    @property
    def neo4j_url(self):
        return get('neo4j_url')

    @property
    def neo4j_user(self):
        return get('neo4j_user')

    @property
    def neo4j_password(self):
        return get('neo4j_password')


config: Config = Config()

import os
set_environment(os.environ.get('ENVIRONMENT', 'local'))