import os
print("[INFO] Loading kernel")
with open('kernel.py', 'r') as f:
    exec(f.read())

