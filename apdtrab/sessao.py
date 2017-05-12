import controle_sessao
#import é salvo nesta variavel para ser usado somente nesse modulo com esse nome
cs = controle_sessao

def imprimir_sessao(lista_sessao):
    print("codigo sessão",lista_sessao[0],"Codigo do filme ",lista_sessao[1]," ","Codigo da Sala ",lista_sessao[2]," ","Horario ",lista_sessao[3])
    print("")

def criar_sessao ():
    cod_sessao = int(input("Digite o cod da sessao"))
    s = cs.criar_sessao(cod_sessao)
    if s == True:
        print("Sessão foi criada")
    else:
        print("erro!!!")
def deletar_sessao():
    cod = str(input("Digito o codigo da sessão a ser deletada"))
    result= cs.remover_sessao(cod)
    if (result == True):
        print("A sessão foi deletada")
    else:
        print("Sessão não encontrada!!")

def listar_sessao():
    sessao = cs.listar_sessao()
    #for s in sessao:
    print(sessao)
        #imprimir_sessao(s)

def buscar_sessao():
    print("Buscar por codigo de sessão")
    cod = str (input("Digite o codigo da Sessão"))
    s = cs.buscar_sessao(cod)
    if ( s == None ):
        print("Sessão n encontrada")
    else:
        print(s)
        #imprimir_sessao(s)

def remover_todas_sessoes():
    cs.remover_todas_sessoes()

def mostrar_sessao():
    run_sessao = True
    menu =("\n----------------\n"+
             "(1) Adicionar nova sessão \n" +
             "(2) Listar Sessão \n" +
             "(3) Buscar Sessão \n" +
             "(4) Remover Sessão \n" +
             "(5) Remover Todas as sessões \n"+
             "(0) Sair\n"+
            "----------------")
    while(run_sessao == True):
        print(menu)
        op = int (input("Escolha uma opção "))
        if (op == 1):
            criar_sessao()
        elif (op == 2):
            listar_sessao()
        elif (op == 3):
            buscar_sessao()
        elif (op == 4):
            remover_sessao()
        elif (op == 5):
            remover_todas_sessoes()
        elif (op == 0):
            run_sessao = False

mostrar_sessao()