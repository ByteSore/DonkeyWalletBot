#!/usr/bin/python
from configparser import ConfigParser
from pprint import pprint
import psycopg2
import json

def global_config(filename='config.ini', section='global'):
    return getconfig(filename, section)

def dbconfig(filename='config.ini', section='postgresql'):
    return getconfig(filename, section)

def getconfig(filename, section):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    conf = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            if param[1].startswith("["):
                conf[param[0]] = json.loads(param[1])
            else:
                conf[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return conf
