import controle_sessao
cs = controle_sessao
#se executar o gerar ingresso ele vai abrir somente uma vez pois precisa das listas atualizados da session
#executando o modulo gerar com aa listas teste, ocorrera que duplicara os dados
lista_ingressos = [[1, 'Alien', 14],
[2, 'Guardiões da Galaxia', 16, 2, 'Guardiões da Galaxia', 16]
,[3, 'machete', 0, 3, 'machete', 0, 3, 'machete', 0]]

lista_ingressos_vendidos = [[1, 'Alien', 14],[2, 'Guardiões da Galaxia', 16]]

def gerar_ingresso(cod_ingresso,ingresso_bruto):
    # ingresso_bruto = cs.listar_sessao()
    #acima recebe a sessão com tudo
    # for x in range (0,len(ingresso_bruto)): #agora eu estou criado um ingresso referente ao primeiro filme vinculado na lista
    #     cod_ingresso = int (input("Codigo do ingresso a ser criado: "))
    horario = ingresso_bruto[0][3] #aqui o horario do filme
    lista_filme = ingresso_bruto[0][1]#Aqui extraio a lista dos filmes
    lista_sala = ingresso_bruto[0][2]#Ja aqui a da sala
    lotacao = lista_sala [1]#aqui retiro o numero de cadeiras de cada sala
    filme_nome = lista_filme[1]#e aqui o nome do filme
    ingresso = [cod_ingresso,filme_nome,horario]
    lista_ingressos.append(ingresso*lotacao)#aqui ele cria o numero de ingressos referentes ao numero de lotação da sala
    ingresso_bruto.remove(ingresso_bruto[0])#nessa parte eu excluo a primeira sessão aquela na posição zero e é substituida pela proxima
    #e indo assim por diante.
    #Me desculpem, mas optei por deixar muitas variaveis para deixar a interface bem nítida pra mim se poluio muito pode fazer alteraçes
    print("Foram Gerados")

def venda_ingresso_meia(cont):
    cod_ingresso = int(input('codigo da sessao: '))
    cont = cont
    intuito = "add-vendas"
    remover_ingresso(cod_ingresso,cont,intuito)
    # ingresso = buscar_ingresso(cod_ingresso)
    # for contidade in range (0,cont):
    #     for x in range (0,3):
    #         vendido = ingresso [0]
    #         lista_ingressos_vendidos.append(vendido)
    #         ingresso.remove(vendido)
    # lista_ingressos = ingresso

def venda_ingresso_inteira(cont):
    cod_ingresso = int(input('codigo da sessao: '))
    cont = cont
    intuito = "add-vendas"
    remover_ingresso(cod_ingresso, cont, intuito)

def listar_ingresso():
    return lista_ingressos

def buscar_ingresso(cod_ingresso):
    for i in lista_ingressos:
        if i[0] == cod_ingresso:
            return i
    return None

def remover_ingresso(cod_ingresso,qtd,intuito):
    if(intuito == "add-vendas"):#esse aqui é onde os modulos vendas vai requisitar a saida
        ingresso = buscar_ingresso(cod_ingresso)
        for contidade in range(0, qtd):
            for x in range(0, 3):
                vendido = ingresso[0]
                lista_ingressos_vendidos.append(vendido)
                ingresso.remove(vendido)
        lista_ingressos = ingresso
    elif(intuito == "retirar"): #quando se retirar sem comprar por ordem do cinema ou seila so tira n entra na lista compra.
        ingresso = buscar_ingresso(cod_ingresso)
        for contidade in range(0, qtd):
            for x in range(0, 3):
                vendido = ingresso[0]
                ingresso.remove(vendido)
        lista_ingressos = ingresso
        print("Bloco excluido")

def remover_todos_ingressos():
    global lista_ingressos
    lista_ingressos = []

def listar_ingressos_vendidos():
    return lista_ingressos_vendidos

def retornar_sessao():
    r =cs.listar_sessao()
    return r