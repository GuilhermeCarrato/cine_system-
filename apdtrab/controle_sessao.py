#import filme
#import sala
lista_sessao = []
def criar_sessao (cod_sessao, cod_filme , horario , cod_sala):
    lista_sessao.append([cod_sessao, cod_filme,cod_sala,horario])
    print("Sessão foi Criada")

def remover_sessao (cod_sessao):
    for s in range (0,len(lista_sessao)):
        if (s[0] == cod_sessao):
            lista_sessao.remove(s)
            return True
    return False

def listar_sessao():
    return lista_sessao

def buscar_sessao(cod_sessao):
    for s in range (0,len(lista_sessao)):
        if s == cod_sessao:
            return s
    return None

def remover_todas_sessoes ():
    global lista_sessao
    lista_sessao =[]
    print("Todas Sessõe Foram Apagadas")

def ingresso():
    return lista_sessao

#def iniciar_lista_ingressos():