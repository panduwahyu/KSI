import string

#Brute Force
cipher_txt = input("Masukkan teks yang akan di-decrypt : ")

def decrypt_txt(key, text):
    decrypted_txt = ""
    alphabet = string.ascii_letters
    for char in text:
        if char.isalpha():
            decrypted_char = alphabet[(alphabet.index(char) - key) % 26]
            decrypted_txt += decrypted_char
        else:
            decrypted_txt += char
    return decrypted_txt
            
for key in range(1, 26):
    decrypted_txt = decrypt_txt(key, cipher_txt)
    print("Hasil Dekripsi : ", decrypted_txt, "||| Key : ", key)
