import logging
import os
from datetime import datetime
from datetime import timedelta

def CleanBackup(backupPath: str, backupDays: int, logs: logging):
    files = os.scandir(backupPath)
    total = 0
    removed = 0
    for f in files:
        if f.is_file() and f.name.endswith(".pdf"):
            # last modified time
            stats = os.stat(f.path)
            currentTime = datetime.now()
            dif: timedelta = currentTime - datetime.fromtimestamp(stats.st_mtime)         
            total += 1
            
            if dif.days > int(backupDays):
                RemoveFile(f.path)
                removed += 1
                logs.info(f"Soubor {f.name} byl odstraněn ze zálohy")
    logs.info(f"Celkem {total} souborů načteno a z toho {removed} vymazáno")
                

def RemoveFile(path: str):
    os.remove(path)