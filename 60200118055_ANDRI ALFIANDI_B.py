class mahasiswa :

    def inputMahasiswa(self):
        self.nama = input("Masukkan Nama : ")
        self.nim = input("Masukkan NIM : ")
    def cetakMahasiswa(self):
        print("NIM : " , self.nim)
        print("Nama : " , self.nama)

class Reguler(mahasiswa) :

    biayaPerSks = 75000

    def __init__(self , semester , jumlahsks , biayaDaftarUlang , danaKemahasiswaan , BOP):
        self.semester = semester
        self.jumlahsks = jumlahsks
        self.biayaDaftarUlang = biayaDaftarUlang
        self.danaKemahasiswaan = danaKemahasiswaan
        self.BOP = BOP


    def entryReguler(self):
        if self.jumlahsks > 24 :
            bool = 0
        else :
            bool = 1
        return bool

    def hitungReguler(self):
        self.totalUangSks = self.jumlahsks * self.biayaPerSks
        self.totalPembayaran = self.biayaDaftarUlang + self.totalUangSks + self.danaKemahasiswaan + self.BOP

        if self.totalPembayaran >= 4500000 :
            self.diskon = self.totalPembayaran * 5 / 100
        else :
            self.diskon = 0

        self.totalBayar = self.totalPembayaran - self.diskon

    def cetakReguler(self):
        super().cetakMahasiswa()
        print("semester : " , self.semester)
        print("Biaya Per Sks : " , self.biayaPerSks)
        print("Dana BOP : " , self.BOP)
        print("Total Sks : " , self.jumlahsks)
        print("Total Pembayaran : " , self.totalPembayaran)
        print("Diskon : " , self.diskon)
        print("Total Yang Harus Di bayarkan : " , self.totalBayar)

class Eksekutif(mahasiswa) :
    biayaPerSks = 120000
    biayaPermataKuliah = 100000

    def __init__(self , periode , biayaAngsuranBOP , jumlahsks1 , jumlahMatakuliah):
        self.periode = periode
        self.biayaAngsuranBOP = biayaAngsuranBOP
        self.jumlahsks1 = jumlahsks1
        self.jumlahMatakuliah = jumlahMatakuliah


    def entryEksekutif(self):
        if self.jumlahsks1 > 24:
            bool = 0
        else:
            bool = 1
        return bool

    def hitungEksekutif(self):
        self.totalUangSks = self.biayaPerSks * self.jumlahsks1
        self.totalBiayaUjian = self.jumlahMatakuliah * self.biayaPermataKuliah
        self.totalPembayaran = self.biayaAngsuranBOP + self.totalUangSks + self.totalBiayaUjian

        if self.totalPembayaran >= 2500000 :
            self.diskon = self.totalPembayaran * 5 / 100
        else:
            self.diskon = 0

        self.totalBayar = self.totalPembayaran - self.diskon
    def cetakEksekutif(self):
        super().cetakMahasiswa()
        print("Periode : " , self.periode)
        print("Biaya Angsuran BOP : " , self.biayaAngsuranBOP)
        print("Jumlah Sks : " , self.jumlahsks1)
        print("Jumlah Matakuliah : " , self.jumlahMatakuliah)
        print("Biaya Per Sks : " , self.biayaPerSks)
        print("Total Pembayaran : " , self.totalPembayaran)
        print("Diskon : " , self.diskon)
        print("Total Yang Dibayar : " , self.totalBayar)

print("Pilih Kelas : ")
print("1.Kelas Reguler")
print("2.Kelas Eksekutif")
pil = int(input("Silahkan Pilih : "))

if pil == 1 :

    print("====================Data Reguler=======================")
    semester = int(input("Input Semester : "))
    jumlahsks = int(input("Input Jumlah Sks : "))
    biayaDaftarUlang = int(input("Input Biaya Daftar Ulang : "))
    danaKemahasiswaan = int(input("Input Dana Kemahasiswaan : "))
    bop = int(input("Dana BOP : "))

    Reg = Reguler(semester , jumlahsks , biayaDaftarUlang , danaKemahasiswaan , bop)
    Reg.inputMahasiswa()
    print()
    print()

    if Reg.entryReguler() == 1 :
        print("Kwitansi Pembayaran Kelas Reguler")
        print("=================================")
        Reg.hitungReguler()
        Reg.cetakReguler()
        print()
    else :
        print("jumlah sks maksimal 24 silahkan coba kembali")
        print("Terima Kasih")

elif pil == 2 :

    print("====================Data Eksekutif=======================")

    periode = input("Input Periode : ")
    biayaAngsuranBOP = int(input("Input Biaya Angsuran BOP : "))
    jumlahsks1 = int(input("Input Jumlah Sks : "))
    jumlahMataKuliah = int(input("Jumlah Matakuliah : "))

    VIP = Eksekutif(periode , biayaAngsuranBOP , jumlahsks1 , jumlahMataKuliah)
    VIP.inputMahasiswa()
    print()
    print()

    if VIP.entryEksekutif() == 1 :

        print()
        print("Kwitansi Pembayaran Kelas Eksekutif")
        print("====================================")
        VIP.hitungEksekutif()
        VIP.cetakEksekutif()
    else:
        print("jumlah sks maksimal 24 silahkan coba kembali")
        print("Terima Kasih")
else :
    print("Pilihan Tidak Ada Silahkan Ulang Kembali")
    print("Terima Kasih")


