from db import criar_tabelas, adicionar_cliente, listar_clientes

 # (Executar somente a primeira vêz)
criar_tabelas()

adicionar_cliente("João Silva", "joao@email.com", "11999999999")
adicionar_cliente("Maria Souza", "maria@email.com", "11888888888")

clientes = listar_clientes()
print("Clientes Cadastrados:")
for c in clientes:
    print(c)
