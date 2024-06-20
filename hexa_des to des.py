def hexa_des(hexa):
    length=len(hexa)
    sum=0
    j=0
    for i in range(length-1,-1,-1):
        if hexa[i]>='0' and hexa[i]<='9': 
            sum=sum+(ord(hexa[i])-48)*pow(16,j)
            j=j+1
        elif hexa[i]>='A' and hexa[i]<='F': 
            sum=sum+(ord(hexa[i])-55)*pow(16,j)
            j=j+1
    return sum 
hexa=input("Enter Any Hexadesimal Number ")
print("Decimal Value of Hexa ",hexa,"=",hexa_des (hexa))