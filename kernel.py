import os

def setupsystem():
    try:
        with open("etc/systemrun", 'r') as f:
            exec(f.read())
    except IOError:
        print("[ERROR] systemrun not found")
