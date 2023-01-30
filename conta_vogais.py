def conta_vogais(vogal):
    qtd = 0
    for letra in vogal:
        if letra.lower() in 'aeiou':
            qtd += 1
    return qtd