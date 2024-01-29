import os
with open("etc/shell", 'r') as f:
    shell = f.readline()
    if shell == "mushroom":
        import bin.mushroom as mushroom
        mushroom.console()
    elif shell == "ish":
        import bin.ish as ish
        ish.console()
    else:
        exec("bin/"+shell+".py")