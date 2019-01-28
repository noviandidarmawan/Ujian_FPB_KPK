#mencari FPB dan KPK dari 2 angka
def hitung_FPB(a, b):
    if a > b:
        pilih = b
    else:
        pilih = a
    for i in range(1, pilih+1):
        if((a % i == 0) and (b % i == 0)):
            fpb = i
    return fpb

def hitung_KPK(a,b):
    dum_1 = 1
    dum_2 = 1
    p = a* dum_1
    q = b* dum_2
    while p != q:
        while p > q:
            dum_2 = dum_2 + 1
            q = b * dum_2
        while p < q:
            dum_1 = dum_1 + 1
            p = a * dum_1
    if p == q:
       return (p)


num1 = int(input("Ketik angka pertama: "))
num2 = int(input("Ketik angka kedua: "))
print('FPB dari '+ str(num1)+ ' dan '+ str(num2)+ ' adalah = ' + str(hitung_FPB(num1,num2)))
print('KPK dari '+ str(num1)+ ' dan '+ str(num2)+ ' adalah = ' + str(hitung_KPK(num1,num2)))


