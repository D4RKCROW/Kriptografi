
abjad = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',  #membuat aray yang berisi abjad A sampai Z
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

key = int(input('Masukkan cipher key yang anda inginkan (dalam angka, misal 9): ')) #menentukan key yang akan digunakan dalam metode caesar cipher

def Caesar_cipher(kalimat,cipher_key): # membuat fungsi yang bertujuan untuk menerapkan caesar cipher
  kalimat = kalimat.upper() # membuat variable kalimat dan berisi huruf kapital
  hasil_Caesar_cipher = '' # membuat variable string untuk memuat hasil enkripsi
  for karakter in kalimat: # membuat perulangan untuk mengenkripsi kalimat
    if karakter in abjad:
      index_lama = abjad.index(karakter) # index lama adalah index pada array abjad
      index_baru = (index_lama + cipher_key ) % len(abjad) # membuat index baru dengan menggeser sejauh key yang telah ditentukan dengan batas index 26
      abjad_baru = abjad[index_baru] # membuat abjad baru dari index baru yang telah diperoleh 
      hasil_Caesar_cipher = hasil_Caesar_cipher + abjad_baru # membuat variable baru yang memuat hasil enkripsi
    else:
       hasil_Caesar_cipher = hasil_Caesar_cipher + " " # jika karakter yang dimasukkan bukan berasal dari abjad A - Z maka akan menjadi spasi
  return hasil_Caesar_cipher # mengembalikan hasil enkripsi


print("Masukkan pilihan")
print("1. Enkripsi")
print("2. Dekripsi")
pil = int(input()) # membuat pilihan untuk melakukan enkripsi atau dekripsi
if pil == 1:
  kalimat = input('Masukkan kalimat yang ingin dienkripsi : ') # memasukkan kalimat yang akan di enkripsi
  kalimat_hasil = Caesar_cipher(kalimat,key) # memanggil fungsi Caesar_cipher untuk mengenkripsi kalimat
  print('Kalimat yang dimasukkan adalah:',kalimat)
  print('Hasil enkripsi kalimat menggunakan Caesar Cipher dengan key:',key, 'adalah', kalimat_hasil) # Menampilkan hasil enkripsi
  
elif pil == 2:
  kalimat_enkripsi = input('Masukkan kalimat yang ingin didekripsi : ') # Memasukkan kalimat yang akan di dekripsi
  kalimat_awal = Caesar_cipher(kalimat_enkripsi,-key) # memanggil fungsi Caesar_cipher untuk mendekripsi kalimat
  print('Hasil Dekripsi Kalimat menggunakan Caesar chiper dengan key negatif adalah:',-key, 'adalah', kalimat_awal) # Menampilkan hasil dekripsi

else:
  print("Pilihan yang anda masukkan salah") # menampilkan kalimat tersebut jika pilihan salah
