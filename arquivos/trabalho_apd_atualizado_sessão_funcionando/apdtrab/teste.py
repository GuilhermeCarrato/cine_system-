lista = [[1,32132,"fsfes",["Rnaldo",157],432],[2,324324,444,'FESF']]
l2 =[2213123,"lista2","lista2 test","fuck"]
l3 =[]
cod=2
def buscar_sessao(cod_sessao):
    for s in lista:
        if s[0] == cod_sessao:
            return s
            break
    print("Não da sa porra")
result = buscar_sessao(cod)
print(result)

