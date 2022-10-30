def encriptar(mensaje):
    texto = []
    texto_encriptado = " "

    for i in range(len(mensaje)):
        texto_encriptado += hashlib.sha256(i.encode('ASCII')).hexdigest()[:8]
    return ''.join(texto)
def desencriptar(mensaje):
    texto = []
    for i in range(len(mensaje)):
        texto.append(desencriptar[hash_desencriptar(mensaje[i])])

    return ''.join(texto)
