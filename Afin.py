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
