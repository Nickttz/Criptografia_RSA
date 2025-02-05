# Criptografia RSA

Este projeto em Python implementa a criptografia RSA **sem o uso de bibliotecas externas**, ou seja, todas as operações são feitas a partir do zero. O código realiza a criptografia de uma mensagem que está em um arquivo `mensagem.txt`, utilizando a geração de chaves e números primos via teste de primalidade Miller-Rabin, além de álgebra modular para a criptografia e descriptografia.

## Estrutura do Projeto

### **Arquivos Python (`.py`)**

- **`criptografia.py`**: Neste arquivo, os arquivos de chaves pública e privada são lidos e a criptografia ou descriptografia da mensagem é realizada. A chave pública é usada para criptografar e a chave privada para descriptografar.

- **`gerar_chave.py`**: Responsável pela geração das chaves pública e privada. A função `gerarChave()` gera os números primos necessários, calcula o módulo `n`, a função totiente de Euler `φ(n)` e, a partir disso, gera as chaves pública `(e, n)` e privada `(d, n)`.

- **`gerar_primo.py`**: Este arquivo contém a lógica para gerar os números primos `p` e `q`. A geração dos primos é feita com o **teste de primalidade Miller-Rabin**, que é eficiente para verificar se um número é primo, garantindo primos fortes e difíceis de serem fatorados.

- **`main.py`**: Arquivo principal que orquestra o processo de criptografia e descriptografia. Ele chama as funções necessárias, manipula os arquivos de entrada e saída, e realiza a criptografia/descriptografia da mensagem.

### **Arquivos de Texto (`.txt`)**

- **`mensagem.txt`**: Contém a mensagem original que será criptografada. Este arquivo é lido pelo programa para aplicar a criptografia RSA.

- **`mensagem_criptografada.txt`**: Arquivo gerado após a criptografia da mensagem. Contém a mensagem criptografada, que pode ser compartilhada com segurança.

- **`mensagem_descriptografada.txt`**: Após a descriptografação da mensagem com a chave privada, o arquivo contém a mensagem original restaurada.

### **Arquivos PEM (`.pem`)**

- **`public_key.pem`**: Contém a chave pública usada para criptografar as mensagens. A chave pública pode ser compartilhada livremente.

- **`private_key.pem`**: Contém a chave privada usada para descriptografar as mensagens. A chave privada deve ser mantida em segurança e não compartilhada.

## Como Funciona

### **1. Geração de Chaves**

A criptografia RSA depende de duas chaves:

- **Chave pública**: Usada para criptografar a mensagem.
- **Chave privada**: Usada para descriptografar a mensagem.

Para gerar as chaves, são escolhidos dois números primos aleatórios `p` e `q`. O módulo `n` é calculado como o produto desses primos (`n = p * q`). Em seguida, calcula-se a função totiente de Euler `φ(n)` e escolhe-se um valor `e` que seja coprimo com `φ(n)`. Com isso, a chave privada `d` é obtida como o inverso multiplicativo de `e` módulo `φ(n)`.

### **2. Criptografia e Descriptografia**

- **Criptografia**: A mensagem é convertida em um número e criptografada utilizando a fórmula:
  \[
  C = $M^e$ $mod$ $n$
  \]
  onde:
  - \( M \) é a mensagem original convertida para número,
  - \( e \) é a chave pública,
  - \( n \) é o módulo.

- **Descriptografia**: A mensagem criptografada é restaurada utilizando a fórmula:
  \[
  M = $C^d$ $mod$ $n$
  \]
  onde:
  - \( C \) é a mensagem criptografada,
  - \( d \) é a chave privada.

### **3. Geração de Números Primos**

A segurança do RSA depende da escolha de números primos grandes. O código utiliza o **teste de primalidade Miller-Rabin** para gerar primos fortes, que são mais difíceis de serem fatorados. Para gerar primos maiores e aumentar a segurança da criptografia, basta aumentar o parâmetro na geração dos primos.

Por exemplo, atualmente os primos estão sendo gerados com o parâmetro `10`:
```python
p = prime.gerar_primo(10)
q = prime.gerar_primo(10)
