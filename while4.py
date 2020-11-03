suma=0
produs=1
nr=1
n=eval(input("Introduceti un numar : "))
while nr<=n :
    suma+=nr
    produs*=nr
    nr+=1

print("Suma numerelor este : ",suma)
print("Produsul numerelor este : ",produs)
print("Media aritmetica a numerelor este : ",suma/n)
