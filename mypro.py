import replace
n0 = 0.1
list = [0.3, 0.5, 0.7, 0.9, 1.2, 1.4, 1.6, 1.8, 2.0, 3.0, 5.0]

for i in range(11):
    n = list[i]
    originalfile = 'R_80_25_1,01.inp'
    replace.replace(originalfile, n0, n)




