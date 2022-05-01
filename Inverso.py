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

a=int(input())
n=int(input())
print(inv(a,n))