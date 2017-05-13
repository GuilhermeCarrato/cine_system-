lista = [[1 ,2,[ 1 , "Alien" , "2 horas" , "18", "Ridley Scott", "tando faz", "cartas","Terror"],["12" , 2], 14], [2 ,3,[ 1 , "Guardiões da Galaxia" , "2 horas" , "18", "Ridley Scott", "tando faz", "cartas","Terror"],["12" , 3 ], 16],[1,2],[2,4],[3,4]]
l2 =[[4,2],[5,4],[6,7],[8,9],[0,1],[2,3]]
l2[1].append("Meia entrada"*1)
print(l2)
for x in range (0,1):
    print(x)


    for s in range (0,len(lista_ingressos)):
        if (s[0] == cod_ingresso):
            lista_ingressos.remove(s)
            return True
    return False