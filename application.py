import configparser
import os
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import shutil

# ----------------------------------------------------------------------------------
def LoadConfiguration():
    try:
        cfg = configparser.ConfigParser()
        cfg.read("config.ini", "UTF-8")
        global _source 
        _source = cfg["DEFAULT"]["SourcePath"]
        global _destination
        _destination = cfg["DEFAULT"]["DestinationPath"]
        global _prefix
        _prefix = cfg["DEFAULT"]["Prefix"]
        global _bartype
        _bartype = cfg["DEFAULT"]["BarcodeType"]
    except:
        print("Zkontroluj jestli je správně nastavená konfigurace! [soubor config.ini]")
        quit()
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
def ConvertToImage():
    LoadConfiguration()
    
    files = os.scandir(_source)
    for t in files:
        if t.is_file() and t.name.endswith(".pdf"):            
            print(f"{t.name} is {t.path}")
            images = convert_from_path(t.path, last_page=3)
            try:
                for d in decode(images[0], symbols=[DetectBarcodeType()]):
                    name: str = d.data.decode("utf-8")
                    new_path = f"{ _destination }\\{name}.pdf"
                    if name.startswith(_prefix):
                        print(f"{name} is of type: {d.type}")
                        shutil.copyfile(t.path, new_path)
                        os.remove(t.path)
            except:
                print("error")
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
def DetectBarcodeType():
    if _bartype == "CODE128":
        return ZBarSymbol.CODE128
    elif _bartype == "CODE39":
        return ZBarSymbol.CODE39
    elif _bartype == "CODE93":
        return ZBarSymbol.CODE93
    elif _bartype == "EAN8":
        return ZBarSymbol.EAN8
    elif _bartype == "EAN13":
        return ZBarSymbol.EAN13
    elif _bartype == "PDF417":
        return ZBarSymbol.PDF417
    else:
        return ZBarSymbol.QRCODE
# ----------------------------------------------------------------------------------