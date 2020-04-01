from src.service.data_dump_service import DollsDump, YamlDumper, JsonDumper
from src.service.dolls_service import DollsScrapingRepository

yamlDump = DollsDump(DollsScrapingRepository(), YamlDumper())
yamlDump.dump_file()

jsonDump = DollsDump(DollsScrapingRepository(), JsonDumper())
jsonDump.dump_file()
