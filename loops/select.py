with open("INDX.txt", "r") as f:
    with open("LINE.txt", "r") as n:
        line = n.readlines()
        indx = f.readlines()
        with open("SEC_STRUCT.txt","w") as w:
            for i, lines in enumerate(line):
                for j,indxes in enumerate(indx):
                    a = lines.split()
                    b = indxes.split()
                    c = "".join(b)
                    
                    if j < 21:
                        res = a[1][int(c)-1]     
                        w.write(c + " " + res +"\n")
                    else:                    
                        w.write(c  +" max \n")                    

        w.close()
    n.close()
f.close()


     
