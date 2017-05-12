import controlador_ingresso
ci = controlador_ingresso
def imprimir_ingresso (ingresso):
    nome = 'nome do cinema'
    filme = 'nome do filme'
    print(nome.upper())
    print(filme.upper())
    print("sala","      ","horario")

def menu_gerar():
    cod_ingresso = str(input("Codigo do ingresso "))
    cod_sessao = int(input("O codigo da sessao escolhida "))
    ci.gerar_ingresso(cod_ingresso,cod_sessao)

def menu_lista():
    ingressos = ci.listar_ingresso()
    for i in ingressos:
        imprimir_ingresso(i)

def menu_busca():
    print("Buscar por codigo do ingresso")
    cod = str(input("Digite o codigo"))
    i = ci.buscar_ingresso(cod)
    if i == None:
        print("Esse ingresso n existe")
    else:
        imprimir_ingresso(i)

def remover_todos_ingressos():
    ci.remover_todos_ingressos()

def remover_ingresso():
    cod = str(input("Digito o codigo do ingresso a ser deletado"))
    result = cs.remover_ingresso(cod)
    if (result == True):
        print("A ingresso foi deletada")
    else:
        print("Ingresso não encontrada!!")

def mostrar_ingresso():
    run_ingresso = True
    menu =("\n----------------\n"+
             "(1) Adicionar nova ingresso \n" +
             "(2) Listar ingresso \n" +
             "(3) Buscar ingresso \n" +
             "(4) Remover ingresso \n" +
             "(5) Remover Todas as sessões \n"+
             "(0) Sair\n"+
            "----------------")
    while(run_ingresso == True):
        print(menu)
        op = int (input("Escolha uma opção "))
        if (op == 1):
            menu_gerar()
        elif (op == 2):
            menu_lista()
        elif (op == 3):
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 5):
            remover_todos_ingressos()
        elif (op == 0):
            run_ingresso = False

mostrar_ingresso()
