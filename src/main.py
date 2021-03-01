from fila_normal import filanormal
from fila_prioritaria import FilaPrioritaria

# f = filanormal()
# f.atualizafila()
# f.atualizafila()
# f.atualizafila()
# f.atualizafila()
# f.atualizafila()
#
# print(f.chamacliente(5))
# print(f.chamacliente(2))

f2 = FilaPrioritaria()
f2.atualiza_fila()
f2.atualiza_fila()
f2.atualiza_fila()

print(f2.chama_cliente(2))
print(f2.chama_cliente(10))
print(f2.estatistica("28", 1007, ""))
print(f2.estatistica("28", 1007, "detail"))



