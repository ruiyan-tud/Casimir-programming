def replace(originalfile, n0, n):
    updated_lines = []
    with open(originalfile, 'r') as myfile:
        s = 0.003
        x = str("{:.4f}".format(s+n0*s))
        x1 = str("{:.4f}".format(s+n*s))
        y = str("{:.4f}".format(s*n0-s))
        y1 = str("{:.4f}".format(s*n-s))
        z = str("{:.4f}".format(n0*s))
        z1 = str("{:.4f}".format(n*s))
        for line in myfile:    
            if x in line:
                updated_lines.append(line.replace(x, x1))
                print("x changed")
                for line in myfile:    
                    if y in line:
                        updated_lines.append(line.replace(y, y1))
                        print("y changed")
                        for line in myfile:    
                            if z in line:
                                updated_lines.append(line.replace(z, z1))
                                print("z changed")
                            else:
                                updated_lines.append(line)
                    else:
                        updated_lines.append(line) 
            else:
                updated_lines.append(line)

#     with open('R_80_25_1,03.inp', 'w') as newfile:
    name = str(n)
    queue = name.replace(".", "")
    with open("R_80_25_1,"+queue+".inp", 'w') as newfile:  
        for line in updated_lines:
            newfile.write(line)
