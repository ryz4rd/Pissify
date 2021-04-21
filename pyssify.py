import pathlib
import shutil

userdir = pathlib.Path.cwd()

pathFiles = []
pathNames = []
suffixes = []

Multimedia = [".avi", ".mp4", ".mov", ".wmv", ".mp3", ".wav"]
Fotos = [".jpg", ".jpeg", ".png", ".gif", ".svg"]
archivosdeTexto = [".txt", ".csv", ".pdf"]
archivosOffice = [".docx", ".xslx", ".pptx"]
Extra = []


dirNames = ["Multimedia", "Fotos", "Archivos de Texto", "Archivos Office", "Extra"]


for files in pathlib.Path(userdir).rglob("*"):
    if pathlib.Path.is_file(files) == True:
        pathNames.append(files.name)
        pathFiles.append(str(files))
        suffixes.extend(files.suffixes)


# Para eliminar un archvio la ruta debe de ser un path ===> 
# pathlib.Path(VAR) LA VARIABLE VA ENTRE LOS PARENTESIS ==> VAR.unlink()

# Creacion de directorios

for dirname in dirNames:
    if pathlib.Path(dirname).exists() == False:
        pathlib.Path(dirname).mkdir()

sufIndex = []

for suf in suffixes:
    if suf in Multimedia:
        suf = "0"
    elif suf in Fotos:
        suf = "1"
    elif suf in archivosdeTexto:
        suf = "2"
    elif suf in archivosOffice:
        suf = "3"
    else:
        suf = "4"
    sufIndex.extend(suf)


dirPath = []

for d_path in dirNames:
    dirPath.append(f"{str(userdir)}\\{d_path}")

for (file, suf, pName) in zip(pathFiles, sufIndex, pathNames):
    
    folderPath = f"{dirPath[int(suf)]}\\{pName}"
    print(file.name)
    #shutil.move(file,folderPath)



        
