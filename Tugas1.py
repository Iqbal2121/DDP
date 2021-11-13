Total_harga = 0
Total_produk = 0

print("Fitur belanja")

while True :
    nama_produk = input("Masukkan nama produk atau X untuk berhenti : ")
    if nama_produk.upper() == "X": 
        print("Terima kasih. Sampai jumpa kembali.")
        break
    harga_barang = int(input("Masukkan harga barang : "))

    print("Produk " +nama_produk+ " Berhasil ditambahkan dengan harga", harga_barang )

    Total_harga += int(harga_barang)
    Total_produk += 1

print("")
print("Total produk : ", Total_produk)
print("Total harga : ", Total_harga)
print("")

if Total_produk > 0 :
    while True :
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
                        print("Email tidak valid. Silahkan Ulangi.")
                    else :
                        break
                while True :
                    password = input("Masukkan password Anda : ")
                    if len(password) >= 8 and password != password.upper() and password != password.lower() and "@" in password or "!" in password or "#" in password or "$" in password:
                        break
                    else :
                        if len(password) < 8 :
                            print("Password tidak valid. Silahkan ulangi.")
                while True :
                    jenis_kartu = input("Masukkan level kepesertaan Anda : ")
                    if jenis_kartu == "Silver" and Total_produk < 5 :
                        print("Selamat! Anda mendapatkan diskon sebesar 5%")
                        diskon_harga = Total_harga * 0.05
                        break
                    elif jenis_kartu == "Silver" and Total_produk >= 5 :
                        print("Selamat! Anda mendapatkan diskon sebesar 10%")
                        diskon_harga = Total_harga * 0.1
                    elif jenis_kartu == "Gold" and Total_produk < 5 :
                        print("Selamat! Anda mendapatkan diskon sebesar 10%")
                        diskon_harga = Total_harga * 0.1
                    elif jenis_kartu == "Gold" and Total_produk >= 5 :
                        print("Selamat! Anda mendapatkan diskon sebesar 15%")
                        diskon_harga = Total_harga * 0.15
                    elif jenis_kartu == "Diamond" and Total_produk < 5 :
                        print("Selamat! Anda mendapatkan diskon sebesar 15%")
                        diskon_harga = Total_harga * 0.15
                    elif jenis_kartu == "Diamond" and Total_produk >= 5 :
                        print("Selamat! Anda mendapatkan diskon sebesar 20%")
                        diskon_harga = Total_harga * 0.2
                    else :
                        print("Level kepesertaan anda tidak valid. Silahkan ulangi.")

                print("")  
                print("Total harga keseluruhan yang harus dibayar :", Total_harga - diskon_harga)
                print("Terima kasih telah berbelanja di NFElectronics.")