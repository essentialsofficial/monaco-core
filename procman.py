import os
import shutil


with open('etc/shell', 'r') as f:
    if (f.readline() == "mushroom"):
        import bin.mushroom as mushroom
        mushroom.console()
