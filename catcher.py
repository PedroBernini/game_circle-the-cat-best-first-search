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

def gatoNoBeco() :
    cont = 0
    if not can_NE(tuplaGato) :
        cont += 1
    if not can_E(tuplaGato) :
        cont += 1    
    if not can_SE(tuplaGato) :
        cont += 1
    if not can_SW(tuplaGato) :
        cont += 1
    if not can_W(tuplaGato) :
        cont += 1
    if not can_NW(tuplaGato) :
        cont += 1
    
    if cont == 5 :
        return True
    else :
        return False

def bloqueioProximo(gato) :
    if(can_NE(gato)) :
        return move_NE(gato)                      
    elif(can_E(gato)) :
        return move_E(gato)                     
    elif(can_SE(gato)) :
        return move_SE(gato)                       
    elif(can_SW(gato)) :
        return move_SW(gato)                       
    elif(can_W(gato)) :
        return move_W(gato)
    elif(can_NW(gato)) :
        return move_NW(gato)

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

# ----- MANIPULAÇÃO DA LISTA DE VISITADOS ----- #
def add_visitados(visita) :
    tupla = (visita[0], visita[1])
    visitados.append(tupla)    

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

def decidirCaminho(caminhosFinais) :

    # 1. Para cada Caminho, extrair a saída 
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

# ----- VARS ----- #
def organizarSaidas(cat, exits) :
    elementos = len(exits)-1
    ordenado = False
    while not ordenado :
        ordenado = True
        for i in range(elementos) :
          if distance(cat, exits[i]) > distance(cat, exits[i + 1]) :
                temp = exits[i]
                exits[i] = exits[i + 1]
                exits[i + 1] = temp
                ordenado = False
    return exits

gato = (tuplaGato[0], tuplaGato[1])
conjuntoBlocks = list(tuplaBlocks)
conjuntoSaidas = organizarSaidas(gato, tuplaExits)
visitados = list()
caminhosSaidas = list()

# ----- (TÉCNICA 1) PRIMEIRO BLOQUEIO ----- #
def primeiroBloqueio() :
    cantos = [(1,9),(9,9),(9,1),(8,1),(1,1),(2,1)]
    
    for canto in cantos :
        if canto not in conjuntoBlocks :
            return canto
    
    return bloqueioProximo(gato)

# ----- (TÉCNICA 2) SEGUNDO BLOQUEIO ----- #
def segundoBloqueio(cat) :
    if cat == (4,5) :
        if (1,1) not in conjuntoBlocks :
            return (1,1)
        elif (2,1) not in conjuntoBlocks :
            return (2,1)
        else :
            return None
    elif cat == (5,4) :
        return None
    elif cat == (6,5) :
        if (8,1) not in conjuntoBlocks :
            return (8,1)
        elif (9,1) not in conjuntoBlocks :
            return (9,1)
        else :
            return None
    
    elif cat == (4,6) :
        if (1,9) not in conjuntoBlocks :
            return (1,9)
        elif (0,8) not in conjuntoBlocks :
            return (0,8)
        elif (4,10) not in conjuntoBlocks :
            return (4,10)
        else :
            return None
    
    elif cat == (5,6) :
        if (1,9) not in conjuntoBlocks :
            return (1,9)
        if (9,9) not in conjuntoBlocks :
            return (9,9)
        else :
            return None
    
    elif cat == (6,6) :
        if (9,9) not in conjuntoBlocks :
            return (9,9)
        elif (6,10) not in conjuntoBlocks :
            return (6,10)
        elif (10,8) not in conjuntoBlocks :
            return (10,8)
        else :
            return None    
        

# ----- (TÉCNICA 4) BLOQUEIO EFICAZ ----- #
def verificarBloqueioEspecial(caminhosFinais) :

    # 1. Mapeia cantos do tabuleiro
    listaCompleta = [[(1,9)],
                 [(1,8),(2,9),(3,9)],
                 [(9,9)],
                 [(9,8),(8,9),(7,9)],
                 [(8,1),(9,1)],
                 [(6,1),(7,1),(8,2),(9,2)],
                 [(1,1),(2,1)],
                 [(1,2),(2,2),(3,1),(4,1)]]

    # 2. Atribui pontuação (quantidade de bloqueios) para cada canto 
    pontuacao = []    
    cont = 0
    for vetor in listaCompleta :
        for casa in vetor :
            if casa in conjuntoBlocks :
                cont += 1
        pontuacao.append(cont)
        cont = 0

    # 3. Verifica se algum dos melhores caminhos atravessa um canto
    posicoes = []
    for i in range(6, 0, -1):
        for el in range(0,len(pontuacao)) :
            if pontuacao[el] == i :
                posicoes.append(el)

    for caminhoFinal in caminhosFinais :
        for posicao in posicoes :
            for casa in listaCompleta[posicao] :
                if casa in caminhoFinal :
                    if casa != gato :
                        return casa
    return None

# ----- MAIN() ----- #
    
# ----- (TÉCNICA 3) MAPEAR OS MELHORES CAMINHOS ----- #
#def formulaSecreta() :
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

'''Definir um caminho'''
caminhosSaidas = organizarCaminhos(caminhosSaidas)    
caminhosFinais = melhoresCaminhos(caminhosSaidas)
caminhoFinal = decidirCaminho(caminhosFinais) 

'''Condições específicas para redefinir bloqueio'''
if gatoNoBeco() :
    bloqueio = bloqueioProximo(gato)

elif gato == (5,5) and len(conjuntoBlocks) <= 10 :
    bloqueio = primeiroBloqueio()

elif (gato == (4,5) or gato == (4,6) or gato == (5,4) or gato == (5,6) or gato == (6,5) or gato == (6,6)) and (len(conjuntoBlocks) <= 10) and (segundoBloqueio(gato) != None)  :
    bloqueio = segundoBloqueio(gato)    

elif (verificarBloqueioEspecial(caminhosFinais) != None) :
    bloqueio = verificarBloqueioEspecial(caminhosFinais)

else :
    if(len(conjuntoBlocks) > 45) :
        bloqueio = bloqueioProximo(gato)
    else :
        if caminhoFinal[len(caminhoFinal) - 1] == gato :
            bloqueio = bloqueioProximo(gato)
        else :
            bloqueio = caminhoFinal[len(caminhoFinal) - 1]
    
    if(bloqueio == (0,10) or bloqueio == (1,10)) and (1,9) not in conjuntoBlocks and (1,9) != gato :
        bloqueio = (1,9)
        
    elif(bloqueio == (9,10) or bloqueio == (10,10)) and (9,9) not in conjuntoBlocks and (9,9) != gato :
        bloqueio = (9,9)

'''Printar decisão final'''
print(bloqueio)