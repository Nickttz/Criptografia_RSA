def ler_mensagem():
    try:
        # Lê o conteúdo inteiro do arquivo como uma string
        with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
            mensagem = arquivo.read() 

        # Converte a string em uma lista de valores ASCII
        mensagem_ascii = []
        for char in mensagem:
            mensagem_ascii.append(ord(char))
        
        return mensagem_ascii
    except:
        print("Erro ao ler arquivo de texto")

def ler_mensagem_cripto():
    try:
        # Lê o conteúdo inteiro do arquivo como uma string
        with open("mensagem_criptografada.txt", "r", encoding="utf-8") as arquivo:
            mensagem = arquivo.read() 

        # Converte a string em uma lista de valores inteiros
        mensagem_cripto = []
        for valor in mensagem.split():
            mensagem_cripto.append(int(valor))
        
        return mensagem_cripto
    except:
        print("Erro ao ler arquivo de texto")

def escrever_mensagem_descripto(mensagem): 
    try:
        with open("mensagem_descriptografada.txt", "w", encoding="utf-8") as arquivo:
            for valor in mensagem:
                arquivo.write(chr(valor))
        return
    except:
        print("Erro ao salvar arquivo criptografado")

def escrever_mensagem_cripto(mensagem):
    try:
        with open("mensagem_criptografada.txt", "w", encoding="utf-8") as arquivo:
            for valor in mensagem:
                arquivo.write(str(valor) + ' ')
        return
    except:
        print("Erro ao salvar arquivo descriptografado")