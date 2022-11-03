
#!/usr/bin/env python

import os
import sys
import shutil
import subprocess

def main():
    if sys.platform == "win32":
        print("This script is for *nix systems only.")
        return

    if not os.path.exists("build"):
        os.mkdir("build")

    pygame_path = input("Please enter the path to your pygame data folder: ")
    pygame_path = os.path.abspath(pygame_path)

    if not os.path.exists(pygame_path):
        print("That path does not exist.")
        return

    if not os.path.exists(os.path.join(pygame_path, "base.pyd")):
        print("That is not a pygame data folder.")
        return

    if not os.path.exists(os.path.join(pygame_path, "base.pyd")):
        print("That is not a pygame data folder.")
        return

    shutil.copy(os.path.join(pygame_path, "base.pyd"), "build")
    shutil.copy(os.path.join(pygame_path, "pygame_sdl2.dll"), "build")
    shutil.copy(os.path.join(pygame_path, "SDL2.dll"), "build")

    f = open("build/run.sh", "w")
    f.write("#!/bin/sh\n")
    f.write("export PYTHONPATH=%s\n" % pygame_path)
    f.write("python main.py\n")
    f.close()

    subprocess.call(["chmod", "+x", "build/run.sh"])

    print("Done.")

if __name__ == "__main__":
    main()