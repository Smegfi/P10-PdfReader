import os
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import shutil

class Application:
    source = None
    destination = None
    prefix = None
    
    files = None

    def __init__(self, source, destination, prefix) -> None:
        self.source = source;
        self.destination = destination;
        self.prefix = prefix;
    
    def Run(self):
        self.LoadFiles()
        
    def LoadFiles(self):
        try:
            self.files = os.scandir(self.source)
            for f in self.files:
                print(f"Načteno: {f.name}")        
            #self.ConvertToImage()
        except:
            print("Chyba při načítání PDF souborů, ukončuji program")
            quit()

    def ConvertToImage(self):
        for f in self.files:
            if f.is_file():
                images = convert_from_path(f.path)
                try:
                    for d in decode(images[0], symbols=[ZBarSymbol.CODE128]):
                        name: str = d.data.decode("utf-8")
                        new_path = f"{ self.destination }\\{name}.pdf"
                        if name.startswith(self.prefix):
                            print(f"{name} is of type: {d.type}")
                            shutil.copyfile(f.path, new_path)
                except:
                    print("error")

    # def ConvertToImage():
    #     for t in files:
    #         if t.is_file():
    #             print(f"{t.name} is {t.path}")
    #             images = convert_from_path(t.path)
    #             try:
    #                 for d in decode(images[0], symbols=[ZBarSymbol.CODE128]):
    #                     name: str = d.data.decode("utf-8")
    #                     new_path = f"{ _destination }\\{name}.pdf"
    #                     if name.startswith(_prefix):
    #                         print(f"{name} is of type: {d.type}")
    #                         shutil.copyfile(t.path, new_path)
    #             except:
    #                 print("error")
