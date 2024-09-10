import random
alph2= "abcdefghijklopqrstuvwxyzABCDEFGHIJKLOPQRSTUVWXYZ1234567890@"
alph= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
def isprime(num):
    if num > 1:
       
        for i in range(2, (num//2)+1):
           
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
def encrypt(m,l):
    
    enc=""
    for i in alph:
        toadd=random.choice(alph2)
        for i in range(l-1):
            toadd+=random.choice(alph2)
        while toadd in enc:
            toadd=random.choice(alph2)
            for i in range(l-1):
                toadd+=random.choice(alph2)
        enc+=toadd
    
    nm=""
    for i in range(len(m)):
        
        nm+=enc[alph.find(m[i])*l:alph.find(m[i])*l+l]
        
        for k in range(l-1):
            toadd=random.choice(alph2)
            nm+=toadd
        nm+=enc[alph.find(m[i])*l:alph.find(m[i])*l+l]
    enc+="m"+str(l)
    temp=0
    while not isprime(len(nm)):
        temp+=1
        nm=random.choice(alph2)+nm
    enc+=("n"+str(temp))
    print("Message:"+nm)
    print()
    print("Key:"+enc)
    print()
    return (nm,enc)
def unencrypt(m,enc):
    temp2=int(enc[enc.find("n")+1:])
    enc=enc[:enc.find("n")]
    l=int(enc[enc.find("m")+1:])
    m=m[temp2:]
    enc=enc[:enc.find("m")]
    nm=""
    while len(m)>0:
        nm+=alph[int(enc.find(m[0:l])/l)]
        temp=m[0:l]
        m=m[1+l:]
        m=m[m.find(temp)+l:]
    print(nm)
if input("Encrypt or Decrypt: ")=="Encrypt":
    put=input("Enter the message: ")
    encrypt(put,int(input("How many levels?(Warning; to many levels will lag): ")))
else:
    put=input("Enter the message to Decrypt: ")
    unencrypt(put,input("Enter the Key: "))