import random

#Calcula o phi_n do numero primo n
def phi_n(numero): 
    if(primo(numero)==True):
        return numero-1
    else:
        return False

#Verifica se um numero eh primo
def primo(num):
    i=1
    temp=0
    while(i<=num):
        if(num%i==0):
            temp=temp+1
        i=i+1
    if(temp==2):
        return True
    else:
        return False

#Função modular entre dois números
def mod(a,b):
    if(a<b):
        return a
    else:
        c=a%b
        return c

#encriptar um texto
def encriptar(frase,e,n):
    tam=len(frase)
    i=0
    lista=[]
    while(i<tam):
        letra = frase[i]
        k=ord(letra)
        k=k**e
        d=mod(k,n)
        lista.append(d)
        i=i+1
    return lista

#Descriptografa um texto criptografado
def decriptar(cifra,n,d):
    lista=[]
    i=0
    tamanho=len(cifra)
    while i<tamanho:
        decriptado = cifra[i]**d
        texto = mod(decriptado,n)
        letra=chr(texto)
        lista.append(letra)
        i=i+1
    return lista

#Calcula a chave privada
def chave_privada(phi,e):
    d = 0
    while(mod(d*e,phi)!=1):
        d=d+1
    return d


## MAIN
if __name__=='__main__':
    texto = raw_input('Entre com o texto claro: ')
    p= 17
    q=23
    n=p*q
    PHI_de_N=(p-1)*(q-1)
    e= 3
    texto_encriptado = encriptar(texto,e,n)
    print(texto_encriptado)
    d = chave_privada(PHI_de_N,e)
    texto_decriptado = decriptar(texto_encriptado,n,d)
    print(texto_decriptado)
