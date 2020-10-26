n=1
nr=0
suma_p=0
suma_n=0
nr_p=0
nr_n=0
while n<=12:
    nr=eval(input("Introduceti temperatura : "))
    if nr>=0:
        suma_p+=nr
        nr_p+=1
    else:
        suma_n+=nr
        nr_n+=1
    n+=1    

med_p=(suma_p)/(nr_p)
med_n=(suma_n)/(nr_n)            
print("Media pozitiva = ",med_p,",iar media negativa = ",med_n)
     