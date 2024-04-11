import random
import string

def gerar_palavra_aleatoria(tamanho):
    letras = string.ascii_uppercase + 'ÁÉÍÓÚÂÊÔÃÕÀÇ'
    return ''.join(random.choice(letras) for _ in range(tamanho))

print(gerar_palavra_aleatoria(5))
