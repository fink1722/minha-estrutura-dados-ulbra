import PilhaE

p1 = PilhaE.PilhaE(5)

p2 = PilhaE.PilhaE(5)

p1.push('a')
p1.push('b')
p2.push('c')
p2.push('d')

p1.push(p2.ver_topo())
p2.pop()
p1.push(p2.ver_topo())
p2.pop()
print(p1.ver_topo())
p1.pop()
print(p1.ver_topo())

