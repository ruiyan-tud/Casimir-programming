# updated_lines = []
# with open('R_80_25_1,01.inp', 'r') as myfile:
#     n0 = 0.10 
#     n = 0.30 
#     s = 0.003
#     x = str("{:.4f}".format(s+n0*s))
#     x1 = str("{:.4f}".format(s+n*s))
#     y = str("{:.4f}".format(s*n0-s))
#     y1 = str("{:.4f}".format(s*n-s))
#     z = str("{:.4f}".format(n0*s))
#     z1 = str("{:.4f}".format(n*s))
#     print(x,y,z)
#     print(type(x1))
#     for line in myfile:    
#         if x in line:
#             updated_lines.append(line.replace(x, x1))
#             print("x changed")
#             for line in myfile:    
#                 if y in line:
#                     updated_lines.append(line.replace(y, y1))
#                     print("y changed")
#                     for line in myfile:    
#                         if z in line:
#                             updated_lines.append(line.replace(z, z1))
#                             print("z changed")
#                         else:
#                             updated_lines.append(line)
#                 else:
#                     updated_lines.append(line)    
#         else:
#             updated_lines.append(line)

# with open('R_80_25_1,03.inp', 'w') as newfile:
#     for line in updated_lines:
#         newfile.write(line)
        
 



#from tkinter import _flatten
# with open('R_80_25_1,01.inp', 'r') as myfile2:
#     lines=myfile2.readlines()
#     length=len(lines)
#     x = '0.0033'
#     x1 = '0.01'
#     y = '0.0099'
#     y1 = '0.02'
#     for i in range(length):
        
#         if x in lines[i]:
#             lines[i]=x1
#             updated_lines.append(lines[i]+'\n')
            
#         else:
#             updated_lines.append(lines[i])
# myfile2.close
# print(updated_lines)
# updated_lines=list(_flatten(updated_lines))
# print(updated_lines)
# with open('R_80_25_1,03.inp', 'w') as newfile:
#     for line in updated_lines:
#         newfile.write(line)
# #### open file 
# filename='sss.txt'



import replace

n0 = 0.1
n = 0.3
originalfile = 'R_80_25_1,01.inp'

replace.replace(originalfile, n0, n)

