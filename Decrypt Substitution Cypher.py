import string

all_letters= string.ascii_letters
key = int(input("Masukkan key : "))

dict = {}     
for i in range(len(all_letters)):
    dict[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
      

cipher_txt = input("Masukkan teks yang akan di-decrypt : ")
decrypt_txt = []
 
for char in cipher_txt:
    if char in all_letters:
        temp = dict[char]
        decrypt_txt.append(temp)
    else:
        temp = char
        decrypt_txt.append(temp)
         
decrypt_txt = "".join(decrypt_txt)
print("Hasil Dekripsi :", decrypt_txt)