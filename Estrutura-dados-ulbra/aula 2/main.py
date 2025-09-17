import Les

l = Les.Les(5)

l.inserir_inicio("a")
l.inserir_inicio("b")
l.inserir_fim("c")
l.show()

l.remover("d")
l.show()

l.remover("a")
l.show()

if l.removerTF('f'):
    print("f foi removido da lista")
else:
    print("f não estava na lista")

l.show()

if l.removerTF("c"):
    print ("c foi removido da lista")
else:
    print ("c não estava na lista")

l.show()

l.inserir_fim("b")
l.inserir_fim("d")
l.inserir_fim("b")

l.show()

print("a letra b foi removida", l.remove_e_contar("c"), "vezes")

l.show()
