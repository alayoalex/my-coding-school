import os

for fichero in os.listdir("."):
    if os.path.isfile(fichero) and not fichero == 'rename.py':
        newname = fichero.replace("droidboot_","")
        print("File:", newname)
        os.rename(fichero, newname)
        
