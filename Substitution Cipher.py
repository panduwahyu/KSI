import string

all_letters= string.ascii_letters

dict1 = {}
key = int(input("Masukkan key : "))



for i in range(len(all_letters)):
	dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]


plain_txt= input("Masukkan teks yang akan di-encrypt : ")
cipher_txt=[]

for char in plain_txt:
	if char in all_letters:
		temp = dict1[char]
		cipher_txt.append(temp)
	else:
		temp =char
		cipher_txt.append(temp)
		
cipher_txt= "".join(cipher_txt)
print("Hasil Enkripsi : ",cipher_txt)
