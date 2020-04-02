import yaml
import csv


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


class CsvDollDumper():
    def write(self, file_name, data):
        with open(file_name + '.csv', 'w', encoding='utf-8') as file:
            w = csv.writer(file)
            w.writerows([(
                i+1,
                d.name,
                d.type,
                d.star,
                d.time,
                d.link_url,
                d.how_to_get,
                d.image_url) for i, d in enumerate(data)])
