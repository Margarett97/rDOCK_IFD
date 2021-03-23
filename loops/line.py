import os

with open("INFO.txt", "r") as f:
    line = f.readlines()
    with open("LINE.txt","w") as n:
        for i, lines in enumerate(line):
            if lines.startswith("protocols.DsspMover: "):
                n.write(lines)
    n.close()
f.close()
    