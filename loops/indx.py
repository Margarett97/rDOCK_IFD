import os

with open("resi5.txt", "r") as f:
    line = f.readlines()
    with open("INDX.txt","w") as n:
        for i, lines in enumerate(line):
            a = lines.split()
            b = a[1].strip(".A")
            n.write(b+ "\n")
    n.close()       
f.close()    