# Memasukkan nama produk atau mengakhirinya  
Total_harga = 0
Total_produk = 0

print("Fitur belanja")

while True :
    nama_produk = input("Masukkan nama produk atau X untuk berhenti : ")
    if nama_produk.upper() == "X": 
        print("Terima kasih. Sampai jumpa kembali.")
        break
    harga_barang = float(input("Masukkan harga barang : "))

    print("Berhasil menambahkan " +nama_produk+ " dengan harga", harga_barang )

    Total_harga += int(harga_barang)
    Total_produk += 1

print("")
print("Total produk : ", Total_produk)
print("Total harga : ", Total_harga)
print("")

# Menanyakan apakah pennguna merupakan seorang anggota dari NFElectronics.
if Total_produk > 0 :
    kartu_anggota = input("Apakah Anda seorang anggota? (Y/t) : ")
    if kartu_anggota == "t" :
        print("Total harga yang harus dibayar", Total_harga)
        print("Terima kasih telah berbelanja di NFElectronics.")
    else :
        if kartu_anggota == "Y" :
            while True :
                email = input("Masukkan email Anda : ")
                domain = "muha@mail.com"
                if domain[4] not in email :
                    print("Email tidak valid. Ulangi.")
                else :
                    break
            while True :
                password = input("Masukkan password Anda : ")
                if len(password) >= 8 and password != password.upper() and password != password.lower() and "@" in password or "!" in password or "#" in password or "$" in password:
                    break
                else :
                    if len(password) < 8 :
                        print("Password tidak valid. Ulangi.")
# Menanyakan level kepesertaan.
            if kartu_anggota == "Y" :   
                while True :
                    jenis_kartu = input("Masukkan level kepesertaan Anda : ")
                    if jenis_kartu == "Silver" and Total_produk < 5 :
                        print("Selamat! Anda mendapatkan potongan harga sebesar 5%")
                        diskon_harga = Total_harga * 0.05
                        break
                    elif jenis_kartu == "Silver" and Total_produk >= 5 :
                        print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
                        diskon_harga = Total_harga * 0.1
                        break
                    elif jenis_kartu == "Gold" and Total_produk < 5 :
                        print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
                        diskon_harga = Total_harga * 0.1
                        break
                    elif jenis_kartu == "Gold" and Total_produk >= 5 :
                        print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
                        diskon_harga = Total_harga * 0.15
                        break
                    elif jenis_kartu == "Diamond" and Total_produk < 5 :
                        print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
                        diskon_harga = Total_harga * 0.15
                        break
                    elif jenis_kartu == "Diamond" and Total_produk >= 5 :
                        print("Selamat! Anda mendapatkan potongan harga sebesar 20%")
                        diskon_harga = Total_harga * 0.2
                        break
                    else :
                        print("Level kepesertaan anda tidak valid. Silahkan ulangi.")
# Bagian akhir total harga keseluruhan
                print("Total harga keseluruhan yang harus dibayar :", Total_harga - diskon_harga)
                print("Terima kasih telah berbelanja di NFElectronics.")