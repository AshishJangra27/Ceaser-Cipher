x = raw_input("Enter text: ")
key = int(raw_input("Enter the decryption Key: "))

lst = []
ord_lst = []
enc_ord_lst = []
dec_lst = []
dec_txt = ''
marg = 0

for i in range(len(x)):
    lst.append(x[i])
    
for i in range(len(x)):
    ord_lst.append(ord(lst[i]))
    
#print('ORDERED LIST :',ord_lst)

for i in range(len(x)):
    
    if (ord_lst[i] != 32):
        enc_ord_lst.append(ord_lst[i] - key) #///////
    else:
        enc_ord_lst.append(ord_lst[i])
        
    
#print('Encrypted ORDERED LIST :',enc_ord_lst)

for i in range(len(x)):
    if(enc_ord_lst[i] < 97):
        
        marg = 97 - enc_ord_lst[i]
        enc_ord_lst[i] = 123 - marg
    else: 
        pass
#print('Encrypted ORDERED LIST :',enc_ord_lst)

for i in range(len(x)):
    dec_lst.append(chr(enc_ord_lst[i]))
    
#print("Decrypted List:",dec_lst)


for i in range(len(dec_lst)):
    dec_txt = dec_txt + dec_lst[i]
    
print('\n')
print "Decrypted Text: ",dec_txt