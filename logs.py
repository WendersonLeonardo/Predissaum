url = "access.log"
dicLogs = {}
arq = open(url, 'r')
for lin in arq:
    
    #lin = arq.readline().split(' ')
    dia = lin.split(' ')[3][1:18]

    if dia == '':
        continue
    
    if dia not in dicLogs:
        dicLogs[dia] = 0
        #print(dia)
    
    dicLogs[dia] += 1

arq.close()

arq = open('logsDiarios.csv', 'w')
cont = 0
for chave, valor in dicLogs.items():
    arq.write('%d, %d\n' % (cont, valor))
    #print(chave, valor)
    cont += 1

arq.close()
