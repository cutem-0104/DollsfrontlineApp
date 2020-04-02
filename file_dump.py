import csv
from src.service.data_dump_service import DollsDump, YamlDumper
from src.service.dolls_service import DollsScrapingRepository

yamlDump = DollsDump(DollsScrapingRepository(), YamlDumper())
yamlDump.dump_file()

