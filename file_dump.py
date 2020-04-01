from src.service.data_dump_service import *
from src.service.dolls_service import *

yamlDump = DollsDump(DollsScrapingRepository(), YamlDumper())
yamlDump.dump_file()

jsonDump = DollsDump(DollsScrapingRepository(), JsonDumper())
jsonDump.dump_file()
