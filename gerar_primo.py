import random

# Teste de primalidade de Miller-Rabin
def miller_rabin(n, k=40):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Escreve n-1 como 2^r * d
    r = 0 
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Realiza k testes de Miller-Rabin
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # a^d % n
        if x == 1 or x == n - 1:
            continue  # Possível primo
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # Composto
    return True  # Provável primo

# Geração de número primo grande
def gerar_primo(bits):
    while True:
        candidato = random.getrandbits(bits) | (1 << bits - 1) | 1  # Garante que é ímpar e tem o tamanho certo
        if miller_rabin(candidato):
            return candidato