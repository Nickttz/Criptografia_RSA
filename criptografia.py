import mensagem as msg

def criptografar(chave_publica):
    mensagem_ascii = msg.ler_mensagem()
    mensagem_criptografada = []
    e, n = chave_publica
    
    for valor in mensagem_ascii:
        mensagem_criptografada.append(pow(valor, e, n))

    msg.escrever_mensagem_cripto(mensagem_criptografada)
    return

def descriptografar(chave_privada):
    mensagem_criptografada = msg.ler_mensagem_cripto()
    mensagem_descriptografada = []
    d, n = chave_privada
    
    for valor in mensagem_criptografada:
        mensagem_descriptografada.append(pow(valor, d, n))

    msg.escrever_mensagem_descripto(mensagem_descriptografada)
    return