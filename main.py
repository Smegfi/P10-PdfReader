import configparser
import zalohovac
import application
from datetime import datetime

cfg = configparser.ConfigParser()
cfg.read("config.ini", "UTF-8")
runPremistovac = cfg["DEFAULT"]["Premistovac"]
runZalohovac = cfg["DEFAULT"]["Zalohovac"]

start = datetime.now()

if runPremistovac == 1:
    zalohovac.MoveFiles()
if runZalohovac == 1:
    zalohovac.CleanBackup()

application.ConvertToImage()

end = datetime.now()

dif = end - start
print(dif)