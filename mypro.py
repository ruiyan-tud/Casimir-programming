updated_lines = []
with open('R_80_25_1,01.inp', 'r+') as myfile:
    x = '0.0033'
    y = '0.0066'
    for line in myfile:    
        if x in line:
            updated_lines.append(line.replace(x, y))
            print("x changed")
        else:
            updated_lines.append(line)
            print ("none")

with open('new_file', 'w') as newfile:
    for line in updated_lines:
        newfile.write(line)
