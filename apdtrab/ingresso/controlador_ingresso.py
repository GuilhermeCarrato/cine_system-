import controle_sessao
cs = controle_sessao

lista_ingressos = []

listar_ingressos_vendidos = []

def gerar_ingresso(cod_ingresso,cod_sessao):
    lista_sessao = cs.ingresso()
    lista_ingressos.append([cod_ingresso,lista_sessao[cod_sessao]])
    print("O ingresso foi gerado com sucesso")

def venda_ingresso_meia(cod_ingresso):
    for v in range (0,len(lista_ingressos)):
        if (v == cod_ingresso):
            w = v
            listar_ingressos_vendidos.append(lista_ingressos[v])
    lista_ingressos[w].append("meia entrada")

def venda_ingressos_inteira(cod_ingresso):
    for v in range (0,len(lista_ingressos)):
        if (v == cod_ingresso):
            w = v
            listar_ingressos_vendidos.append(lista_ingressos[v])
            print("Entrada inteira aceita")
    lista_ingressos[w].append("meia entrada")

def listar_ingresso():
    return lista_ingressos

def buscar_ingresso(cod_ingresso):
    for i in range (0,len(lista_ingressos)) :
        if i[0] == cod_ingresso:
            return i
    return None

def remover_ingresso(cod_ingresso):
    for s in range (0,len(lista_ingressos)):
        if (s[0] == cod_ingresso):
            lista_ingressos.remove(s)
            return True
    return False

def remover_todos_ingressos():
    global lista_ingressos
    lista_ingressos = []

def listar_ingressos_vendidos():
    return listar_ingressos_vendidos