import gerar_primo as prime

def gerarChave():
    p = prime.gerar_primo(10)
    q = prime.gerar_primo(10)
    n = q * p
    totiente = (p-1) * (q-1)
    e = 65537
    d = inverso_modular(e, totiente)
    
    return (d, n), (e, n)

def inverso_modular(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m 
        x0, x1 = x1 - q * x0, x0  # Troca os valores de x0 e x1
    if x1 < 0: 
        return x1 + m0
    else:
        return x1