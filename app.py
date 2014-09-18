# coding: utf-8

import os
import sys
import yaml
from pkg_resources import load_entry_point


with open('config.yaml') as f:
    os.environ.update(yaml.load(f))
    if 'DOCKER_REGISTRY_CONFIG' in os.environ:
        os.environ['DOCKER_REGISTRY_CONFIG'] = os.path.abspath(os.environ['DOCKER_REGISTRY_CONFIG'])


sys.exit(load_entry_point('docker-registry==0.9.0', 'console_scripts', 'docker-registry')())
