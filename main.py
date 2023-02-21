import configparser
import zalohovac
import application
from datetime import datetime
import logging

cfg = configparser.ConfigParser()
cfg.read("config.ini", "UTF-8")
# Application config load
skenPath = cfg["DEFAULT"]["SkenPath"]
sourcePath = cfg["DEFAULT"]["SourcePath"]
destinationPath = cfg["DEFAULT"]["DestinationPath"]
ginisPath = cfg["DEFAULT"]["GinisPath"]
espisPath = cfg["DEFAULT"]["EspisPath"]
mover = cfg["DEFAULT"]["Premistovac"]
prefix = cfg["DEFAULT"]["Prefix"]
barcodeType = cfg["DEFAULT"]["BarcodeType"]

# Backup config Load
backup = cfg["BACKUP"]["Zalohovac"]
backupPath = cfg["BACKUP"]["BackupPath"]
backupDays = cfg["BACKUP"]["BackupDays"]

# Logger config load
log = cfg["LOG"]["Logger"]
logPath = cfg["LOG"]["LogPath"]

d = datetime.now()
filename = f"{logPath}\\{d.year}-{d.month}-{d.day}--{d.hour}-{d.minute}.log"

logger = logging

if log == "1":
    logger.basicConfig(filename=filename, level=logging.DEBUG,encoding="UTF-8")
    logger.info("Logs are on!")

if mover == "1": 
    if backup == "1":
        application.MoveFiles(skenPath, ginis = ginisPath, espis = espisPath, backup = backupPath, logs=logger)        
    else:
        application.MoveFiles(skenPath, ginis = ginisPath, espis = espisPath, logs=logger)        

    application.ConvertToImage(sourcePath, destinationPath, barcodeType, prefix, logs=logger)

if backup == "1":
    logger.info("Backup is on!")
    zalohovac.CleanBackup(backupPath, backupDays, logs=logger)
else:    
    logger.info("Backup is off or unset!")


# def TestConfig():
#     if sourcePath.count() <= 0:
#         raise AttributeError("[SkenPath] was now found in configuration.")
#     if destinationPath.count() <= 0:
#         raise AttributeError("[DestinationPath] was now found in configuration.")   
#     if barcodeType.count() <= 0:
#         raise AttributeError("[BarcodeType] was now found in configuration.")    
#     if prefix.count() <= 0:
#         raise AttributeError("[Prefix] was now found in configuration.")    
#     else:
#         print("Configuration was loaded")
    
        