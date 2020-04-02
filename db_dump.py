import os
import csv
from src.service.data_dump_service import DollsDump, CsvDollDumper
from src.service.dolls_service import DollsYamlRepository

dbDump = DollsDump(DollsYamlRepository(), CsvDollDumper())
dbDump.dump_file()
