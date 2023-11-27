# Membuat Dictionary daftar kontak
kontak = {'Aldi': '081267888', 'Lili': '087677776'}

# Menampilkan Kontak Aldi
print("Kontak Aldi", kontak['Aldi'])

# Menambahkan kontak RIka
kontak['Rika'] = '087654544'

# Mengubah kontak Lili
kontak['Lili'] = '088999776'

# Tampilkan semua nama
print("=====Menampilkan semua nama=====")
for nama in kontak.keys():
    print(nama)

# Tampilkan semua nomor
print("\n=====Menampilkan semua nomor=====")
for nomor in kontak.values():
    print(nomor)

# Tampilkan daftar Nama dan nomornya
print("\n=====Menampilkan nama dan nomor=====")
for nama, nomor in kontak.items():
    print(f"{nama}: {nomor}")

# Menghapus kontak Lili
del kontak['Lili']
    

