while True:
 print("1. Enkripsi Reverse Cipher\n" + "2. Enkripsi Ceasar Cipher\n" + "3. Dekrispi Ceasar Cipher\n" + "4. Exit")
 menuInput = input("Silahkan pilih layanan yang ingin digunakan: ")
 try:
    menu = int(menuInput)
 except ValueError:
    print("silahkan masukan bilangan bulat (1-4)")
    continue
 
 if (menu == 1):
   message = input("Masukan teks yang ingin di enkripsi :")
   
   translated = '' #cipher text is stored in this variable
   i = len(message) - 1
 
   while i >= 0:
     translated = translated + message[i]
     i = i - 1
   print("Reverse Cipher : ", translated)
   print("\n=====================================================================\n")
 
 elif (menu == 2):
   message = input("Masukan teks yang ingin di enkripsi :")
   s = int(input("masukan Shift pattern untuk Caesar Cipher (bilangan bulat): "))
   def encrypt(message,s):
     result = ""
       # transverse the plain text
     for i in range(len(message)):
      char = message[i]
 
      # Encrypt uppercase characters in plain text
      if (char.isupper()):
        result += chr((ord(char) + s-65) % 26 + 65)
  
      # Encrypt lowercase characters in plain text
      else:
        result += chr((ord(char) + s - 97) % 26 + 97)
  
     return result
   
   print("Enkripsi Ceasar Cipher: " + encrypt(message,s))
   print("\n\n")
 
 elif (menu == 3):
  message = input("Masukan teks enkripsi Ceasar Cipher :")
  s = int(input("masukan Shift pattern: "))
  #fungsi dekripsi
  def decrypt(message,s):
    result = ""
      # transverse the plain text
    for i in range(len(message)):
     char = message[i]
     # Encrypt uppercase characters in plain text
     if (char.isupper()):
       result += chr((ord(char) - s - 65) % 26 + 65)
  
     # Encrypt lowercase characters in plain text
     else:
       result += chr((ord(char) - s - 97) % 26 + 97)
  
    return result
  print("Dekripsi Ceasar Cipher: " + decrypt(message,s))
  print("\n\n")

 elif (menu == 4):
  break
 
 else:
  print("silahkan masukan angka sesuai pilihan yang tersedia (1-4)")

