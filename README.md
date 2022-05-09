# Inverso modular y Cifrado Afin
Nombre: Emmanuel del Piero Martinez Salcedo

El presente repositorio de código python permite encontrar el inverso modular de un número (si existe) y cifrar, descifrar y descifrar por fuerza bruta una palabra

### Inverso modular
En matemáticas , particularmente en el área de la teoría de números , un inverso multiplicativo modular de un número entero "a" es un número entero x tal que el producto "ax" es congruente con 1 con respecto al módulo "m" . En la notación estándar de la aritmética modular, esta congruencia se escribe como: ax ≅ 1 (mod m)

Expresado sin congruencia: ax mod m = 1

### Cifrado Afin
El cifrado afín también se le llama cifrado de transformación afín o cifrado monoalfabético genérico. Es un tipo de cifrado por sustitución en el que cada símbolo del alfabeto en claro (el alfabeto del texto en claro) es sustituido por un símbolo del alfabeto cifrado (el alfabeto del texto cifrado) siendo el número de símbolos del alfabeto en claro igual que el número de símbolos del alfabeto cifrado. Para hallar el símbolo del alfabeto cifrado que sustituye a un determinado símbolo del alfabeto en claro, se usa una función matemática afín en aritmética modular.

Tanto para el cifrado y el decifrado se necesitan unas claves "a" y "b" y un alfabeto de tamaño "n", para el decifrado se necesita que el inverso modular de a exista

#### Cifrado, Decifrado de una letra
Se considera "l" como la posicion de una letra en el alfabeto "n"

l(cifrada) = (a * l(descifrada) + b) mod n

l(decifrada) = (l(cifrada)-b) * Inverso(a,n) mod n

## Funcionamiento
Para el Inverso modular:
El programa necesitara que el usuario ingrese "a" y "n", luego hallara el inverso modular de "a" solo si existe
Para el Cifrado Afin:
El programa pide ingresar las claves "a" y "b" y luego pide ingresar la palabra, posteriormente pide si se quiere cifrar, decifrar o decifrar a la fuerza (mostrara todos los posibles descifrados con todas las claves)

## Código

El cifrado Afin reutiliza códigos ya implementados anteriormente en el curso incluido el código del inverso modular

```python
def Euclides(n,m):
    if m==0:
        return n
    else:
        return Euclides(m,(n%m))  
def EuclidesEXT(n,m):
    if m==0:
        return (n,1,0)
    else:
        (d,x2,y2)=EuclidesEXT(m, n%m)
        (x,y)=(y2,x2-(((n/m)-((n/m)%1))*y2))
        return(d,x,y)

def Inverso(a,n):
    if Euclides(a,n)==1:
        (d,x,y)=EuclidesEXT(a,n)
        return int((x%n))
    else:
        print("No existe el inverso multiplicativo")

def Afin(a,b,c,n):
    Alfabeto=['a','b','c','d','e','f','g','h','i','j','k',
                'l','m','n','ñ','o','p','q','r','s','t','u',
                'v','w','x','y','z']
    c=list(c)
    Cafin=list(c)
    Cafin2=""
    print("Descifrar, Cifrar, Descifrar a la fuerza (0/1/2)")
    aux=int(input())
    if aux==0:
        i=0
        j=0
        while i < 27:
            if (c[j]==Alfabeto[i] and (Euclides(a,27)==1)):
                Cafin[j]=Alfabeto[(i-b)*Inverso(a,27)%n]
                j += 1
                i = -1
                if j==len(Cafin):
                    break
            i += 1
        print("Descifrado:")
    elif aux==1:
        i=0
        j=0
        while i < 27:
            if c[j]==Alfabeto[i]:
                Cafin[j]=Alfabeto[(a*i+b)%n]
                j += 1
                i = -1
                if j==len(Cafin):
                    break
            i += 1
        print("Cifrado:")
    elif aux==2:
        a=1
        b=1
        i=0
        j=0
        k=1
        while a<27:
            while b<=27:
                while i < 27:
                    if (c[j]==Alfabeto[i] and (Euclides(a,27)==1)):
                        Cafin[j]=Alfabeto[(i-b)*Inverso(a,27)%n]
                        j += 1
                        i = -1
                        if j==len(Cafin):
                            for i2 in Cafin:
                                Cafin2 += i2
                            print(k,": ",Cafin2,"(",a,",",b,")")
                            k+=1
                            print(" ")
                            Cafin2=""
                            break
                    i += 1
                i=0
                j=0
                b+=1
            a+=1
            b=1
    if aux==1 or aux==0:
        for i2 in Cafin:
            Cafin2 += i2
        print(Cafin2)

#elementalmiqueridowatson
#okhfsnkfnwfcwjhsnchqywfswf
#slbcmvrbshzbtñsrqvvmszbvhñbvrqvlalhzbtñsrqvwqaxlzwñaqfqv
print("Ingrese clave a y clave b")
a=int(input("a: "))
b=int(input("b: "))
print("Ingrese la palabra a descifrar o cifrar")
c=str(input())
n=27
Afin(a,b,c,n)
```
