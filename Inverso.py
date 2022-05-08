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
        return (int(x%n))
    else:
        print("No existe el inverso multiplicativo")

a=int(input())
n=int(input())
print("Inverso modular: ",Inverso(a,n))
