def Euclides(n,m): #Usando algoritmo de euclides para saber si son coprimos
    if m==0:
        return n
    else:
        return Euclides(m,(n%m))  
def inv(a,n):
    e=Euclides(a,n)
    if e!=1 or n<0:
        print("No existe el inverso multiplicativo") #Si no son coprimos o n es negativo no existe inverso
    elif e==1:
        for x in range(1,n): #Por teoria el inverso se encuentra en un rango de 1 hasta n
            if(((a%n)*(x%n) % n)==1): #Buscamos el menor x que cumpla la condicion:(a mod n)(x mod n) mod n = 1
                return x #Retorna X
def afin(a,b,c,n):
    Alfabeto=['a','b','c','d','e','f','g','h','i','j','k', #Alfabeto de 27 letras
                'l','m','n','ñ','o','p','q','r','s','t','u',
                'v','w','x','y','z']
    c=list(c) #Vuelvo el str(c) en una lista de char
    Cafin=list(c) #Lista de char del mismo tamaño de c donde almacenar resultados
    print("Descifrar o Cifrar (1/0)")
    aux=int(input()) #Aux para elegir cifrar o descifrar
    if aux==1: #Descifrar
        i=0
        j=0
        while i <= 27:#Recorro las letras del alfabeto
            if c[j]==Alfabeto[i]: #Cuando encuentra la posicion de la letra igual a c
                Cafin[j]=Alfabeto[(i-b)*inv(a,27)%n] #Formula para el descifrado afin
                j += 1 #Avanzo a la siguiente letra de C
                i = -1 #Reinicio la lista de letras para comparar con la siguiente letra de C
                if j==len(Cafin): #Cuando ya se evaluaron todas las letras salgo del while
                    break
            i += 1
        print("Descifrado:")
        print(Cafin) #Imprimo descifrado
    elif aux==0:#cifrar
        i=0
        j=0
        while i <= 27:#Recorro las letras del alfabeto
            if c[j]==Alfabeto[i]: #Cuando encuentra la posicion de la letra igual a c
                Cafin[j]=Alfabeto[(a*i+b)%n] #Formula para el cifrado afin
                j += 1 #Avanzo a la siguiente letra de C
                i = -1 #Reinicio la lista de letras para comparar con la siguiente letra de C
                if j==len(Cafin): #Cuando ya se evaluaron todas las letras salgo del while
                    break
            i += 1
        print("Cifrado:")
        print(Cafin) #Imprimo cifrado

n=27  
a=4
b=7
c=str(input())
print(afin(a,b,c,n))