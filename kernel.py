import os

def setupsystem():
    print("[INFO] Starting system")
    try:
        with open("etc/systemrun", 'r') as f:
            exec(f.read())
    except IOError:
        print("[ERROR] systemrun not found")
