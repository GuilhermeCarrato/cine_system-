#import filme
#import sala
sessao_list = []
def criar_sessao (cod_sessao,cod_filme , horario , cod_sala):
    sessao = [cod_sessao, cod_filme , horario , cod_sala]
    sessao_list.append(sessao)

def remover_sessao (cod_sessao):
    for s in sessao_list:
        if (s[0] == cod_sessao):
            sessao_list.remove(s)
            return True
    return False

def listar_sessao():
    return sessao_list

def buscar_sessao(cod_sessao):
    for s in sessao_list:
        if s[0] == cod_sessao:
            return s
            break
    return None

def remover_todas_sessoes ():
    global sessao_list
    sessao_list =[]
    print("Todas Sessõe Foram Apagadas")

def ingresso():
    return sessao_list

def iniciar_lista_ingressos():
    criar_sessao(1,"Alien",1300,12)
    criar_sessao(2,"Guardiões da galaxia",1400,14)
    criar_sessao(3,"Logan",1600,1)