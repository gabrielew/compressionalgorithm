A = '1'
C = '000'
T = '001'
G = '01'

s = input()

sn = s.replace('A', A).replace('C', C).replace('T', T).replace('G', G)

print('{} {:.1f}'.format(sn, 100 - ((len(sn) * 100) / (len(s) * 8 ))))
