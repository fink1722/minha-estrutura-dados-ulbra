import Ldde

l = Ldde.Ldde()
l.inserir_fim('A')
l.inserir_fim('B')
l.inserir_fim('C')
l.inserir_fim('D')
l.inserir_fim('E')
l.inserir_fim('F')
l.inserir_fim('G')
l.inserir_fim('H')
l.inserir_fim('I')
l.inserir_fim('J')

l.show()          # ABCDEFGHIJ
l.show_reverso()  # JIHGFEDCBA

print("Remoção do intervalo [3..5] (remove D,E,F)")
l.remover_intervalo(3, 5)
l.show()          # ABCGHIJ
l.show_reverso()  # JIHGCBA

print("Remoção do intervalo [0..2] (remove A,B,C)")
l.remover_intervalo(0, 2)
l.show()          # GHIJ
l.show_reverso()  # JIHG

print("Testando se a remoção funcionou")
l.inserir_inicio('C')
l.inserir_inicio('B')
l.show()          # BCGHIJ
l.show_reverso()  # JIHGCB

print("Remoção do intervalo [3..5] (remove HIJ)")
l.remover_intervalo(3, 5)
l.show()          # BCG 
l.show_reverso()  # GCB

print("Testando se a remoção funcionou")
l.inserir_fim('H')
l.inserir_fim('I')
l.show()          # BCGHI
l.show_reverso()  # IHGCB

print("Remoção unitária [1..1] (remove apenas a posição 1)")
l.remover_intervalo(1, 1)
l.show()          # BGHI
l.show_reverso()  # IHGB

print("Remoção total [0..3]")
l.remover_intervalo(0, 3)
l.show()          # (vazia)
l.show_reverso()  # (vazia)

l.inserir_fim('A')
l.inserir_fim('B')
l.inserir_fim('C')
l.inserir_fim('D')
l.inserir_fim('E')
l.inserir_fim('F')
l.inserir_fim('G')
l.inserir_fim('H')
l.inserir_fim('I')
l.inserir_fim('J')

print("Intervalos inválidos (não alteram a lista)")
l.remover_intervalo(2, 1)          # início > fim
l.remover_intervalo(-1, 0)         # início < 0
l.show()          # ABCDEFGHIJ
l.show_reverso()  # JIHGFEDCBA


