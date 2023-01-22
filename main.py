import os
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import shutil
import configparser
from application import Application

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
    except:
        print("Zkontroluj jestli je správně nastavená konfigurace! [soubor config.ini]")
        quit()

def ConvertToImage():
    files = os.scandir(_source)
    for t in files:
        if t.is_file():
            print(f"{t.name} is {t.path}")
            images = convert_from_path(t.path, last_page=3)
            try:
                for d in decode(images[0], symbols=[ZBarSymbol.CODE128]):
                    name: str = d.data.decode("utf-8")
                    new_path = f"{ _destination }\\{name}.pdf"
                    if name.startswith(_prefix):
                        print(f"{name} is of type: {d.type}")
                        shutil.copyfile(t.path, new_path)
            except:
                print("error")

if __name__ == "__main__":
    LoadConfiguration()
    ConvertToImage()