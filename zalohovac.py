import os
import shutil
import configparser
from datetime import datetime
from datetime import timedelta

# ----------------------------------------------------------------------------------
def LoadConfiguration():
    try:
        cfg = configparser.ConfigParser()
        cfg.read("config.ini", "UTF-8")
        global _sken 
        _sken = cfg["DEFAULT"]["SkenPath"]        
        global _backup 
        _backup = cfg["DEFAULT"]["BackupPath"]    
        global _ginis 
        _ginis = cfg["DEFAULT"]["GinisPath"]    
        global _espis 
        _espis = cfg["DEFAULT"]["EspisPath"]
    except:
        print("Zkontroluj jestli je správně nastavená konfigurace! [soubor config.ini]")
        quit()
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
def MoveFiles():
    LoadConfiguration()

    files = os.scandir(_sken)
    for f in files:
        if f.is_file() and f.name.endswith(".pdf"):
            shutil.copyfile(f.path, _backup + f"\\{f.name}")
            shutil.copyfile(f.path, _ginis + f"\\{f.name}")
            shutil.copyfile(f.path, _espis + f"\\{f.name}")
            print(f"Soubor {f.name} byl přesunut na příslušná místa")
            RemoveFile(f.path)
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
def CleanBackup():
    LoadConfiguration()

    files = os.scandir(_backup)
    for f in files:
        if f.is_file() and f.name.endswith(".pdf"):
            # last modified time
            stats = os.stat(f.path)
            currentTime = datetime.now()
            dif: timedelta = currentTime - datetime.fromtimestamp(stats.st_mtime)         
            
            if dif.days > 30:
                print(f"Soubor {f.name} je starší 30ti dnů a bude odstraněn")
                RemoveFile(f.path)
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
def RemoveFile(path: str):
    os.remove(path)
# ----------------------------------------------------------------------------------