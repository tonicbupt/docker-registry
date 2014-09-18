# coding: utf-8

import os
import yaml


with open('config.yaml') as f:
    env = yaml.load(f)
    for key, value in env.iteritems():
        if key.isupper():
            os.environ[key] = value
    os.environ['SQLALCHEMY_INDEX_DATABASE'] = 'mysql://{username}:{password}@{host}:{port}/{db}'.format(**env['mysql'])
    os.environ['DOCKER_REGISTRY_CONFIG'] = os.path.abspath(os.environ['DOCKER_REGISTRY_CONFIG'])
    os.environ['CACHE_REDIS_HOST'] = str(env['redis']['host'])
    os.environ['CACHE_REDIS_PORT'] = str(env['redis']['port'])


from docker_registry.wsgi import application
