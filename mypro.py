#good luck!
text = open('R_80_25_1,01.inp', 'r+')
x = " 0.0033 "
y = "-0.0027"
z = " 0.0003 "
xi = " 0.0039 "
yi = " -0.0021 "
zi = " 0.0009 "
for line in text:    
    if x,y,z in line:
        text.write(line.replace(x, xi))
        print line
        text.write(line.replace(y, yi))
        print line
        text.write(line.replace(z, zi))
        print line
    else:
        print line
text.close()
