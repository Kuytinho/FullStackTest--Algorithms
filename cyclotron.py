def cyclotron(particula, tamanho):
    EMPTY = 1
    
    matriz = [[EMPTY] * tamanho for _ in range(tamanho)]
    
    if particula == "e":
        matriz[0] = [particula] * tamanho  # Preenche a primeira linha com "e"
        for i in range(tamanho):
            matriz[i][-1] = particula  # Preenche a última coluna com "e"
    elif particula == "p":
        matriz[0] = [particula] * tamanho  # Preenche a primeira linha com "p"
        matriz[-2][-2] = particula  # Preenche a penúltima linha e penúltima coluna com "p"
        for i in range(tamanho - 1):
            matriz[i][0] = particula  # Preenche a primeira coluna com "p"
            matriz[-1][i] = particula  # Preenche a última linha com "p" em todas as colunas, exceto a última
            matriz[i][-1] = particula  # Preenche a última coluna com "p" em todas as linhas, exceto a última
    elif particula == "n":
        matriz[0] = [particula] * tamanho  # Preenche a primeira linha com "n"
    
    return matriz

