n=0
suma=0
while n%2==0 or n//3!=0:
    n=eval(input("Introduceti un numar : "))
    if n%2==0:
        suma+=n
    
print("Suma nr introduse este : ",suma)