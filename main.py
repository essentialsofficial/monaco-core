import os
with open("etc/systemrun", 'r') as f:
    exec(f.read())