import criptografia as cripto
import gerar_chave as key

chave_privada, chave_publica = key.gerarChave()

with open("public_key.pem", "w") as arquivo:
    arquivo.write(str(chave_publica))

with open("private_key.pem", "w") as arquivo:
    arquivo.write(str(chave_privada))

cripto.criptografar(chave_publica)
print("Criptografia feita!")

cripto.descriptografar(chave_privada)
print("Descriptografia feita!")

