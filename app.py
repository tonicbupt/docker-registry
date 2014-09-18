# coding: utf-8

import os
import yaml
from docker_registry.wsgi import application


class NBEWrapper(object):

    def __init__(self, app):
        self.app = app
        self.load_environ()

    def __call__(self, env, start_response):
        return self.app(env, start_response)

    def load_environ(self):
        with open('config.yaml') as f:
            env = yaml.load(f)
            for key, value in env.iteritems():
                if key.isupper():
                    os.environ[key] = value
            os.environ['SQLALCHEMY_INDEX_DATABASE'] = 'mysql://{username}:{password}@{host}:{port}/{db}'.format(**env['mysql'])
            os.environ['DOCKER_REGISTRY_CONFIG'] = os.path.abspath(os.environ['DOCKER_REGISTRY_CONFIG'])
            os.environ['CACHE_REDIS_HOST'] = str(env['redis']['host'])
            os.environ['CACHE_REDIS_PORT'] = str(env['redis']['port'])


app = NBEWrapper(application)
