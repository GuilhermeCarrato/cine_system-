import controlador_ingresso
ci = controlador_ingresso
# def imprimir_ingresso (ingresso):
#     nome = 'nome do cinema'
#     filme = 'nome do filme'
#     print(nome.upper())
#     print(filme.upper())
#     print("sala","      ","horario")

def menu_listar_vendidos():
    ingressos = ci.listar_ingressos_vendidos()
    for v in ingressos:
        print(v)

def menu_gerar():
    ingresso = ci.retornar_sessao()
    for x in range (0,len(ingresso)):
        cod_ingresso = int(input("Codigo do ingresso a ser criado: "))
        ci.gerar_ingresso(cod_ingresso,ingresso)

def menu_lista():
    ingressos = ci.listar_ingresso()
    for i in ingressos:
        print(i)
        # imprimir_ingresso(i)

def menu_busca():
    print("Buscar por codigo do ingresso")
    cod = int(input("Digite o codigo"))
    i = ci.buscar_ingresso(cod)
    if i == None:
        print("Esse ingresso n existe")
    else:
        print(i)
        #imprimir_ingresso(i)

def remover_todos_ingressos():
    ci.remover_todos_ingressos()

def remover_ingresso():#o erro so acontece quando vc pedi mais do que existe pra sair
    quantidade = int(input("Quanto a ser retirado: "))
    intuito = "retirar"
    cod = int(input("Digito o codigo do ingresso a ser deletado"))
    ci.remover_ingresso(cod, quantidade, intuito)

def menu_vender():#menu criado somente para teste
    cont = int (input("Quantos ingressos no total?: "))
    print("1 - para meia entrada: ")
    print("2 - para inteira: ")
    op  = int (input("Escolha o tipo do ingresso: "))
    if(op == 1):
        ci.venda_ingresso_meia(cont)
    elif(op == 2):
        ci.venda_ingresso_inteira(cont)

def mostrar_ingresso():
    run_ingresso = True
    menu =("\n----------------\n"+
             "(1) Gerar ingressos \n" +
             "(2) Listar ingresso \n" +
             "(3) Buscar ingresso \n" +
             "(4) Remover ingresso \n" +
             "(5) Remover Todas os ingressos \n"+
             "(6) verder ingresso\n"+
             "(7) Listar ingresso vendidos \n" +
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
            menu_busca()
        elif (op == 4):
            remover_ingresso()
        elif (op == 5):
            remover_todos_ingressos()
        elif (op == 6):
            menu_vender()
        elif (op == 7):
            menu_listar_vendidos()
        elif (op == 0):
            run_ingresso = False

mostrar_ingresso()
