import logging
import os
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import shutil


def MoveFiles(skenPath: str, logs: logging, **paths: str):
    files = os.scandir(skenPath)
    index = 0
    for f in files:
        if f.is_file() and f.name.endswith(".pdf"):
            index += 1
            try:
                shutil.copyfile(f.path, paths["ginis"] + f"\\{f.name}")
                shutil.copyfile(f.path, paths["espis"] + f"\\{f.name}")
                if not paths["backup"] == None and paths["backup"].count() <= 0:
                    shutil.copyfile(f.path, paths["backup"] + f"\\{f.name}")
                    logs.info(f"{f.name} byl přesunut")
            except:
                logs.error(f"{f.name} chyba při přesunu souboru")
    if not index > 0:
        logs.info("Nebyl nalezen žádný soubor k přesunutí")
            

def ConvertToImage(source: str, destination: str, barcodeType: str, prefix: str, logs: logging):    
    files = os.scandir(source)
    index = 0
    for f in files:
        if f.is_file() and f.name.endswith(".pdf"):
            index += 1
            images = convert_from_path(f.path, last_page=3)
            try:
                for i in images:
                    codes = decode(i, symbols=[DetectBarcodeType(barcodeType)])
                    
                    if len(codes) <= 0:
                        logs.error(f"{f.name} nebyl nalezen žádný čárový kód")

                    for c in codes:
                        name: str = c.data.decode("utf-8")                    
                        if name.startswith(prefix):
                            new_path = f"{ destination }\\{name}.pdf"
                            shutil.copyfile(f.path, new_path)
                            os.remove(f.path)                        
                            logs.info(f"{f.name} byl načten čárový kód {name}")
                        else:
                            logs.error(f"{f.name} nebyl nalezen čárový kód typu {barcodeType}")
            except:
                raise Exception("Chyba při konvertování pdf")
    if index == 0:
        logs.info("No .pdf files found!")

def DetectBarcodeType(type: str):
    if type == "CODE128":
        return ZBarSymbol.CODE128
    elif type == "CODE39":
        return ZBarSymbol.CODE39
    elif type == "CODE93":
        return ZBarSymbol.CODE93
    elif type == "EAN8":
        return ZBarSymbol.EAN8
    elif type == "EAN13":
        return ZBarSymbol.EAN13
    elif type == "PDF417":
        return ZBarSymbol.PDF417
    elif type == "QRCODE":
        return ZBarSymbol.QRCODE
    elif type.count() <= 0:
        raise Exception("[BarcodeType] nebyl nataven nebo není nalezen, prosím zkontroluj konfiguraci")