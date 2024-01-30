import os
import shutil
import sys

def cf():
    fp = input("Path: ")
    with open(fp, 'w') as f:
        f.write("")

def vf():
    fp = input("Path: ")
    file = open(fp, mode='r', encoding='utf-8')
    print(file.read())

def wf():
    fp = input("Path: ")
    data = input("Data: ")
    with open(fp, 'w') as f:
        f.write(data)

def loadmod():
    modpath = input("Please, enter mod path: ")
    with open(modpath) as f2:
        exec(f2.read())