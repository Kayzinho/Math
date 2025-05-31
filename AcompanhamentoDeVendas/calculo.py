def calcular_totais(matriz):
    totais_semanais = [sum(semana) for semana in matriz]
    totais_produtos = [sum(col) for col in zip(*matriz)]
    return totais_semanais, totais_produtos