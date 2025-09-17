import Ldse

l = Ldse.Ldse()

l.inserir_inicio("a")

l.inserir_inicio("b")

l.inserir_inicio("c")

print("-"*50)
l.show()
print("-"*50)
l.remover_inicio()

print("-"*50)
l.show()
print("-"*50)

l.inserir_inicio("d")

l.show()





print("-"*50)
l.remover_fim()

l.show()

l.remover('d')
print("-"*50)


l.inserir_inicio("a")
l.inserir_fim('j')
l.show()
print("-"*50)
l.remover('b')
l.show()
