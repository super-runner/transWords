import os
import shutil

EXE_DIR = "dist/"
EXE_NAME = "transWords.exe"
EXE_PATH = EXE_DIR + EXE_NAME

if __name__ == "__main__":
    os.system("pyinstaller.exe -w -F -i Canada.ico  transWords.py")

    if os.path.exists(EXE_PATH):
        if os.path.exists("transWords.exe"):
            os.remove("transWords.exe")
        shutil.move(EXE_PATH, EXE_NAME)

    if os.path.exists("build"):
        shutil.rmtree("build")

    if os.path.exists("dist"):
        shutil.rmtree("dist")

    if os.path.exists("transWords.spec"):
        os.remove("transWords.spec")
