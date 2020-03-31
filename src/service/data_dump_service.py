import yaml
import json
from src.service.dolls_service import DollsScrapingRepository
from datetime import datetime


class DollsDump():
    def __init__(self, repository, dumper):
        self.repository = repository
        self.dumper = dumper

    def dump_file(self):
        self.dumper.write('data/dolls_out', self.repository.result)


class YamlDumper():
    def write(self, file_name, data):
        with open(file_name + '.yaml', 'w') as file:
            yaml.dump(data, file)


class JsonDumper():
    def write(self, file_name, data):
        def expireEncoda(object):
            if isinstance(object, datetime):
                return object.isoformat()

        with open(file_name + '.json', 'w') as file:
            json.dump(json.dumps(data, default=expireEncoda), file)


dd = DollsDump(DollsScrapingRepository(), JsonDumper())
dd.dump_file()

