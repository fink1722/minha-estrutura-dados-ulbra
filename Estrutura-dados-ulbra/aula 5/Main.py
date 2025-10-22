import Ldsec


l = Ldsec.Ldsec()


l.inserir_inicio('a')

l.inserir_fim('b')



l.show()

l.remover_inicio()

l.show()


l.inserir_inicio('a')

l.inserir_fim('c')

l.show()

l.remover_fim()

l.show()
l.inserir_fim('c')
l.inserir_fim('d')
l.remover_antes('c')

l.show()
