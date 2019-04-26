# ----- AUTORES ----- #
# Felipe Carreiro Marchi
# Pedro Henrique Bernini Silva

# ----- BIBLIOTECAS ----- #
import importlib
import sys

# ----- ARQUIVO CONFIGS ----- #
tuplaGato = eval(sys.argv[1])
tuplaBlocks = eval(sys.argv[2])
tuplaExits = eval(sys.argv[3])

# ----- VARS ----- #
gato = (tuplaGato[0], tuplaGato[1])
conjuntoBlocks = list(tuplaBlocks)
conjuntoSaidas = list(tuplaExits)
visitados = list()
caminhosSaidas = list()

# ----- VALIDADORES DE POSIÇÃO ----- #
def valid(cat) :
    if (cat[0] < 0 or cat[0] > 10 or
        cat[1] < 0 or cat[1] > 10 or
        cat in conjuntoBlocks) :
        return False
    return True

def cat_escape(cat) :
    if(cat in tuplaExits) :
        return True
    return False

# ----- VALIDADORES DE MOVIMENTO ----- #
def can_NE(cat) :
    if(cat[0] % 2 == 1) :
        cat = (cat[0] - 1, cat[1] + 1)
    else :
        cat = (cat[0] - 1,cat[1])
    return valid(cat)

def can_E(cat) :
    cat = (cat[0],cat[1] + 1)
    return valid(cat)

def can_SE(cat) :
    if(cat[0] % 2 == 1) :
       cat = (cat[0] + 1, cat[1] + 1)
    else :
        cat = (cat[0] + 1, cat[1])
    return valid(cat)

def can_SW(cat):
    if(cat[0] % 2 == 1) :
        cat = (cat[0] + 1, cat[1])
    else :
        cat = (cat[0] + 1, cat[1] - 1)
    return valid(cat)

def can_W(cat) :
    cat = (cat[0],cat[1] - 1)
    return valid(cat)

def can_NW(cat):
    if(cat[0] % 2 == 1) :
        cat = (cat[0] - 1, cat[1])
    else :
        cat = (cat[0] - 1, cat[1] - 1)
    return valid(cat)

# ----- OUTROS VALIDADORES ----- #
def isNeighbor(primeira, segunda) :
    if(primeira[0] % 2 == 0) :
        if(primeira[0] == segunda[0] + 1 and primeira[1] == segunda[1]) :#NE
            return True
        elif(primeira[0] == segunda[0] and primeira[1] == segunda[1] - 1) :#E
            return True
        elif(primeira[0] == segunda[0] - 1 and primeira[1] == segunda[1]) :#SE
            return True
        elif(primeira[0] == segunda[0] - 1 and primeira[1] == segunda[1] + 1) :#SW
            return True
        elif(primeira[0] == segunda[0] and primeira[1] == segunda[1] + 1) :#W
            return True
        elif(primeira[0] == segunda[0] + 1 and primeira[1] == segunda[1] + 1) :#NW
            return True
        else :
            return False
    else :
        if(primeira[0] == segunda[0] + 1 and primeira[1] == segunda[1] - 1) :#NE
            return True
        elif(primeira[0] == segunda[0] and primeira[1] == segunda[1] - 1) :#E
            return True
        elif(primeira[0] == segunda[0] - 1 and primeira[1] == segunda[1] - 1) :#SE
            return True
        elif(primeira[0] == segunda[0] - 1 and primeira[1] == segunda[1]) :#SW
            return True
        elif(primeira[0] == segunda[0] and primeira[1] == segunda[1] + 1) :#W
            return True
        elif(primeira[0] == segunda[0] + 1 and primeira[1] == segunda[1]) :#NW
            return True
        else :
            return False

# ----- MOVIMENTAÇÃO ----- #
def move_NE(cat) :
    if(cat[0] % 2 == 1) :
        cat = (cat[0] - 1, cat[1] + 1)
    else :
        cat = (cat[0] - 1,cat[1])
    return cat  

def move_E(cat) :
    cat = (cat[0],cat[1] + 1)
    return cat

def move_SE(cat) :
    if(cat[0] % 2 == 1) :
       cat = (cat[0] + 1, cat[1] + 1)
    else :
        cat = (cat[0] + 1, cat[1])
    return cat

def move_SW(cat) :
    if(cat[0] % 2 == 1) :
        cat = (cat[0] + 1, cat[1])
    else :
        cat = (cat[0] + 1, cat[1] - 1)
    return cat

def move_W(cat) :
    cat = (cat[0],cat[1] - 1)
    return cat

def move_NW(cat):
    if(cat[0] % 2 == 1) :
        cat = (cat[0] - 1, cat[1])
    else :
        cat = (cat[0] - 1, cat[1] - 1)
    return cat

# ----- MANIPULAÇÃO DAS LISTAS DE VISITADOS E DE SAÍDAS ----- #
def add_visitados(visita) :
    tupla = (visita[0], visita[1])
    visitados.append(tupla)

def add_caminhosSaidas(caminhoInteiro) :
    visitados.append(caminhoInteiro)

# ----- FUNÇÕES SOBRE DISTÂNCIAS ----- #
def distance(cat, finish) :
    diference = finish[1] - cat [1] # Diferenca de colunas
    if(cat[0] == finish[0]) :
        return abs(diference)

    if(cat[0] % 2 == 1) : # Caso o gato estiver em linha ímpar
        if(abs(cat[0] - finish[0]) == 1) : # Diferenca de 1 linha
            if(diference <= 0) :
                return abs(diference) + 1
            else :
                return abs(diference)
            
        if(abs(cat[0] - finish[0]) == 2) : # Diferenca de 2 linhas
            if(diference == 0) :
                return 2
            else :
                return abs(diference) + 1
            
        if(abs(cat[0] - finish[0]) == 3) : # Diferenca de 3 linhas
            if(diference >= -1 and diference <= 2) :
                return 3
            elif(diference > 0) :
                return abs(diference) + 1
            elif(diference < 0) :
                return abs(diference) + 2
               
        if(abs(cat[0] - finish[0]) == 4) : # Diferenca de 4 linhas
            if(diference >= -2 and diference <= 2) :
                return 4
            else :
                return abs(diference) + 2
           
        if(abs(cat[0] - finish[0]) == 5) : # Diferenca de 5 linhas
            if(diference >= -2 and diference <= 3) :
                return 5
            elif(diference > 0) :
                return abs(diference) + 2
            elif(diference < 0) :
                return abs(diference) + 3
           
        if(abs(cat[0] - finish[0]) == 6) : # Diferenca de 6 linhas
            if(diference >= -3 and diference <= 3) :
                return 6
            else :
                return abs(diference) + 3
            
        if(abs(cat[0] - finish[0]) == 7) : # Diferenca de 7 linhas
            if(diference >= -3 and diference <= 4) :
                return 7
            elif(diference > 0) :
                return abs(diference) + 3
            elif(diference < 0) :
                return abs(diference) + 4
           
        if(abs(cat[0] - finish[0]) == 8) : # Diferenca de 8 linhas
            if(diference >= -4 and diference <= 4) :
                return 8
            else :
                return abs(diference) + 4
            
        if(abs(cat[0] - finish[0]) == 9) : # Diferenca de 9 linhas
            if(diference >= -4 and diference <= 5) :
                return 9
            elif(diference > 0) :
                return abs(diference) + 4
            elif(diference < 0) :
                return abs(diference) + 5
           
    else : # Caso o gato estiver em linha par
        if(abs(cat[0] - finish[0]) == 1) : # Diferenca de 1 linha
            if(diference >= 0) :
                return abs(diference) + 1
            else :
                return abs(diference)
            
        if(abs(cat[0] - finish[0]) == 2) : # Diferenca de 2 linhas
            if(diference == 0) :
                return 2
            else :
                return abs(diference) + 1
            
        if(abs(cat[0] - finish[0]) == 3) : # Diferenca de 3 linhas
            if(diference >= -2 and diference <= 1) :
                return 3
            elif(diference > 0) :
                return abs(diference) + 2
            elif(diference < 0) :
                return abs(diference) + 1
               
        if(abs(cat[0] - finish[0]) == 4) : # Diferenca de 4 linhas
            if(diference >= -2 and diference <= 2) :
                return 4
            else :
                return abs(diference) + 2
           
        if(abs(cat[0] - finish[0]) == 5) : # Diferenca de 5 linhas
            if(diference >= -3 and diference <= 2) :
                return 5
            elif(diference > 0) :
                return abs(diference) + 3
            elif(diference < 0) :
                return abs(diference) + 2
           
        if(abs(cat[0] - finish[0]) == 6) : # Diferenca de 6 linhas
            if(diference >= -3 and diference <= 3) :
                return 6
            else :
                return abs(diference) + 3
            
        if(abs(cat[0] - finish[0]) == 7) : # Diferenca de 7 linhas
            if(diference >= -4 and diference <= 3) :
                return 7
            elif(diference > 0) :
                return abs(diference) + 4
            elif(diference < 0) :
                return abs(diference) + 3
           
        if(abs(cat[0] - finish[0]) == 8) : # Diferenca de 8 linhas
            if(diference >= -4 and diference <= 4) :
                return 8
            else :
                return abs(diference) + 4
            
        if(abs(cat[0] - finish[0]) == 9) : # Diferenca de 9 linhas
            if(diference >= -5 and diference <= 4) :
                return 9
            elif(diference > 0) :
                return abs(diference) + 5
            elif(diference < 0) :
                return abs(diference) + 4
           
        if(abs(cat[0] - finish[0]) == 10) : # Diferenca de 10 linhas
            if(diference >= -5 and diference <= 5) :
                return 10
            else :
                return abs(diference) + 5
            
def melhoraDistancia(cat, distancia, lado, saida):
    if(lado == "NE") :
        inicio = move_NE(cat)
    elif(lado == "E") :
        inicio = move_E(cat)
    elif(lado == "SE") :
        inicio = move_SE(cat)
    elif(lado == "SW") :
        inicio = move_SW(cat)
    elif(lado == "W") :
        inicio = move_W(cat)
    elif(lado == "NW") :
        inicio = move_NW(cat)
    
    novaDistancia = distance(inicio,saida)
    
    if novaDistancia == None :
        return False
    else :
        if novaDistancia < distancia :
            return True
        else:
            return False

def pioraDistancia(cat, distancia, lado, saida):
    if(lado == "NE") :
        inicio = move_NE(cat)
    elif(lado == "E") :
        inicio = move_E(cat)
    elif(lado == "SE") :
        inicio = move_SE(cat)
    elif(lado == "SW") :
        inicio = move_SW(cat)
    elif(lado == "W") :
        inicio = move_W(cat)
    elif(lado == "NW") :
        inicio = move_NW(cat)
    
    novaDistancia = distance(inicio,saida)
    
    if novaDistancia == None :
        return True
    else :
        if novaDistancia > distancia:
            return True
        else:
            return False

# ----- MANIPULAÇÃO DE ROTAS ----- #
def melhorarCaminho(sequencia) :
    quantidade = range(len(sequencia))
    for i in quantidade :
        tamanho = len(sequencia) - 1
        while(tamanho > i + 1) :
            if(isNeighbor(sequencia[i],sequencia[tamanho])) :
                del sequencia[i+1:tamanho]
                quantidade = range(len(sequencia))
                i = 0
                break
            tamanho -= 1
    return sequencia

def mostrarCaminho(ultima, atual) :
    if(ultima[0] % 2 == 0) :
        if(ultima[0] == atual[0] + 1 and ultima[1] == atual[1]) :
            return "NE"
        elif(ultima[0] == atual[0] and ultima[1] == atual[1] - 1) :
            return "E"
        elif(ultima[0] == atual[0] - 1 and ultima[1] == atual[1]) :
            return "SE"
        elif(ultima[0] == atual[0] - 1 and ultima[1] == atual[1] + 1) :
            return "SW"
        elif(ultima[0] == atual[0] and ultima[1] == atual[1] + 1) :
            return "W"
        elif(ultima[0] == atual[0] + 1 and ultima[1] == atual[1] + 1) :
            return "NW"
    else :
        if(ultima[0] == atual[0] + 1 and ultima[1] == atual[1] - 1) :
            return "NE"
        elif(ultima[0] == atual[0] and ultima[1] == atual[1] - 1) :
            return "E"
        elif(ultima[0] == atual[0] - 1 and ultima[1] == atual[1] - 1) :
            return "SE"
        elif(ultima[0] == atual[0] - 1 and ultima[1] == atual[1]) :
            return "SW"
        elif(ultima[0] == atual[0] and ultima[1] == atual[1] + 1) :
            return "W"
        elif(ultima[0] == atual[0] + 1 and ultima[1] == atual[1]) :
            return "NW"

def organizarCaminhos(caminhosSaidas) :
    elementos = len(caminhosSaidas)-1
    ordenado = False
    while not ordenado :
        ordenado = True
        for i in range(elementos) :
          if len(caminhosSaidas[i]) > len(caminhosSaidas[i + 1]) :
                temp = caminhosSaidas[i]
                caminhosSaidas[i] = caminhosSaidas[i + 1]
                caminhosSaidas[i + 1] = temp
                ordenado = False
    return caminhosSaidas

def melhoresCaminhos(caminhos) :
    osMelhores = []
    tamanho = len(caminhos[0])
    i = 0
    while(len(caminhos[i]) == tamanho) :
        osMelhores.append(caminhos[i])
        i += 1
        if(len(caminhos) - 1 < i) :
            break
    
    return osMelhores
        

# ----- (TÉCNICA 2) PRIMEIRO MOVIMENTO ----- #
def primeiroMovimento() :
    
    # 1. Separa os cantos do tabuleiro
    canto1 = [(0,8),(0,9),(0,10),(1,8),(1,9),(1,10),(2,9),(2,10),(3,9),(3,10),(4,10)]
    canto2 = [(10,8),(10,9),(10,10),(9,8),(9,9),(9,10),(8,9),(8,10),(7,9),(7,10),(6,10)]
    canto3 = [(10,0),(10,1),(10,2),(10,3),(9,0),(9,1),(9,2),(8,0),(8,1),(8,2),(7,0),(7,1),(6,0),(6,1),(5,0)]
    canto4 = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,1),(4,0),(4,1),(5,0)]

    # 2. Atribui pontuação para cada canto
    pontuacao1 = 0
    for casa in canto1 :
        if casa in conjuntoBlocks :
            if casa == (1,9) :
                pontuacao1 += 0.18
            else :
                pontuacao1 += 0.09
                
    pontuacao2 = 0
    for casa in canto2 :
        if casa in conjuntoBlocks :
            if casa == (9,9) :
                pontuacao2 += 0.18
            else :
                pontuacao2 += 0.09
                
    pontuacao3 = 0
    for casa in canto3 :
        if casa in conjuntoBlocks :
            if casa == (1,1) or casa == (2,1) :
                pontuacao3 += 0.1
            else :
                pontuacao3 += 0.066
                
    pontuacao4 = 0
    for casa in canto4 :
        if casa in conjuntoBlocks :
            if casa == (8,1) or casa == (9,1) :
                pontuacao4 += 0.1
            else :
                pontuacao4 += 0.066

    conjunto1 = [pontuacao1, "canto1"]
    conjunto2 = [pontuacao2, "canto2"]
    conjunto3 = [pontuacao3, "canto3"]
    conjunto4 = [pontuacao4, "canto4"]
    
    cantos = [conjunto1, conjunto2, conjunto3, conjunto4]

    # 3. Ordena cantos por pontuação 
    elementos = len(cantos)-1
    ordenado = False
    while not ordenado :
        ordenado = True
        for i in range(elementos) :
            conjunto1 = cantos[i]
            conjunto2 = cantos[i + 1]
            if conjunto1[0] > conjunto2[0] :
                temp = conjunto1[0]
                conjunto1[0] = conjunto2[0]
                conjunto2[0] = temp
                
                temp = conjunto1[1]
                conjunto1[1] = conjunto2[1]
                conjunto2[1] = temp
                ordenado = False
        
    # 4. Se puder, direciona gato ao melhor canto
    for el in cantos :
        canto = el[1]
        if(canto == "canto1" and (4,6) not in conjuntoBlocks) :
            return "NE"
        elif(canto == "canto2" and (6,6) not in conjuntoBlocks) :
            return "SE"
        elif(canto == "canto3" and (6,5) not in conjuntoBlocks) :
            return "SW"
        elif(canto == "canto4" and (4,5) not in conjuntoBlocks) :
            return "NW"

# ----- (TÉCNICA 3) DECISÃO DE MOVIMENTOS ----- #
def decidirCaminho(caminhosFinais) :
    
    # 1. Pegar saída de cada caminho
    casasDeSaida = []
    for el in caminhosFinais:
        for i in range(len(el)) :
            if(i == len(el) -1) :
                casasDeSaida.append(el[i])
    
    # 2. Para cada saída, obter uma pontuação em relação a distância entre outras saídas
    pontuacaoSaidas = []
    for saidaFinal in casasDeSaida :
        pontuacao = 0
        for saida in conjuntoSaidas :
            if(saida not in conjuntoBlocks) :
                pontuacao += distance(saidaFinal, saida)
        pontuacaoSaidas.append(pontuacao)

    # 3. Pega a saída com menor pontuação (a mais próxima das outras)  
    posicao = 0
    menorPontuacao = pontuacaoSaidas[0]
    for i in range(len(pontuacaoSaidas)) :
        if(pontuacaoSaidas[i] < menorPontuacao) :
            menorPontuacao = pontuacaoSaidas[i]
            posicao = i
            
    return caminhosFinais[posicao]

# ----- MAIN() ----- #
#conjuntoSaidas = list(set(conjuntoSaidas))
#conjuntoSaidas.remove((0,4))
#conjuntoSaidas.remove((0,5))
#conjuntoSaidas.remove((0,6))
#conjuntoSaidas.remove((0,7))
#conjuntoSaidas.remove((10,4))
#conjuntoSaidas.remove((10,5))
#conjuntoSaidas.remove((10,6))
#conjuntoSaidas.remove((10,7))

# ----- (TÉCNICA 1) MAPEAR OS MELHORES CAMINHOS ----- #
for saidaPrincipal in conjuntoSaidas :
    cat = (tuplaGato[0], tuplaGato[1])
    visitados = []
    loops = 0
    
    '''Considerar looping infinito apos 150 loops'''
    while not cat_escape(cat) and loops < 150 :
        loops += 1
        
        add_visitados(cat)
        distancia = distance(cat, saidaPrincipal)        
        
        #Anda se melhorar a distancia
        if (melhoraDistancia(cat,distancia,"NE",saidaPrincipal) and can_NE(cat) and move_NE(cat) not in visitados) :
            cat = move_NE(cat)
        elif (melhoraDistancia(cat,distancia,"E",saidaPrincipal) and can_E(cat) and move_E(cat) not in visitados) :
            cat = move_E(cat)      
        elif (melhoraDistancia(cat,distancia,"SE",saidaPrincipal) and can_SE(cat) and move_SE(cat) not in visitados) :
            cat = move_SE(cat)       
        elif (melhoraDistancia(cat,distancia,"SW",saidaPrincipal) and can_SW(cat) and move_SW(cat) not in visitados) :
            cat = move_SW(cat)    
        elif (melhoraDistancia(cat,distancia,"W",saidaPrincipal) and can_W(cat) and move_W(cat) not in visitados) :
            cat = move_W(cat)
        elif (melhoraDistancia(cat,distancia,"NW",saidaPrincipal) and can_NW(cat) and move_NW(cat) not in visitados) :
            cat = move_NW(cat)

        #Anda se não piorar a distancia
        else :
            if (not pioraDistancia(cat,distancia,"NE",saidaPrincipal) and can_NE(cat) and move_NE(cat) not in visitados) :
                cat = move_NE(cat)         
            elif (not pioraDistancia(cat,distancia,"E",saidaPrincipal) and can_E(cat) and move_E(cat) not in visitados) :
                cat = move_E(cat)     
            elif (not pioraDistancia(cat,distancia,"SE",saidaPrincipal) and can_SE(cat) and move_SE(cat) not in visitados) :
                cat = move_SE(cat)          
            elif (not pioraDistancia(cat,distancia,"SW",saidaPrincipal) and can_SW(cat) and move_SW(cat) not in visitados) :
                cat = move_SW(cat)        
            elif (not pioraDistancia(cat,distancia,"W",saidaPrincipal) and can_W(cat) and move_W(cat) not in visitados) :
                cat = move_W(cat)
            elif (not pioraDistancia(cat,distancia,"NW",saidaPrincipal) and can_NW(cat) and move_NW(cat) not in visitados) :
                cat = move_NW(cat)
            
            #Anda se ainda não foi visitado
            else :
                if(can_NE(cat) and move_NE(cat) not in visitados) :
                    cat = move_NE(cat)
                elif(can_E(cat) and move_E(cat) not in visitados) :
                    cat = move_E(cat)
                elif(can_SE(cat) and move_SE(cat) not in visitados) :
                    cat = move_SE(cat)
                elif(can_SW(cat) and move_SW(cat) not in visitados) :
                    cat = move_SW(cat)
                elif(can_W(cat) and move_W(cat) not in visitados) :
                    cat = move_W(cat)
                elif(can_NW(cat) and move_NW(cat) not in visitados) :
                    cat = move_NW(cat)                
                
                #Vai na fé 
                else :
                    if(can_NE(cat)) :
                        cat = move_NE(cat)                     
                    elif(can_E(cat)) :
                        cat = move_E(cat)                    
                    elif(can_SE(cat)) :
                        cat = move_SE(cat)                    
                    elif(can_SW(cat)) :
                        cat = move_SW(cat)                    
                    elif(can_W(cat)) :
                        cat = move_W(cat)
                    elif(can_NW(cat)) :
                        cat = move_NW(cat)
                    
    add_visitados(cat)
    
    '''Melhorar os caminhos que não entraram em looping'''
    if(len(visitados) < 150) :
        visitados = melhorarCaminho(visitados)
        
    caminhosSaidas.append(visitados)

'''Ordenar os Caminhos de Saídas por tamanho'''
caminhosSaidas = organizarCaminhos(caminhosSaidas)

#Printar decisão do primeiro movimento
primeiroMov = primeiroMovimento()
if gato == (5,5) and len(conjuntoBlocks) <= 10 and primeiroMov != None :
    print(primeiroMov)

#Ou printar decisão genérica
else :
    caminhosFinais = melhoresCaminhos(caminhosSaidas)    
    caminhoFinal = decidirCaminho(caminhosFinais)    
    print(mostrarCaminho(caminhoFinal[0],caminhoFinal[1]))