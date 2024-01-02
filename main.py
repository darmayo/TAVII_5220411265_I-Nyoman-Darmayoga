class Kendaraan:
    def __init__(self, nama, bensin):
        # Atribut dengan access modifier private
        self.__nama = nama
        self.__bensin = bensin
 
    # Getter untuk mengakses atribut private
    def get_nama(self):
        return self.__nama
 
    def get_bensin(self):
        return self.__bensin
 
    def set_bensin(self, bensin):
        self.__bensin = bensin
 
    def cek_bensin(self):
        if self.__bensin <= 0:
            print(f"{self.__nama}: Bensin habis!")
        else:
            print(f"{self.__nama}: Bensin masih tersedia.")
 
    def hitung_jarak_maksimal(self, liter_bensin, konsumsi_perliter):
        return liter_bensin * konsumsi_perliter
 
 
class Mobil(Kendaraan):
    def __init__(self, nama, bensin, jumlah_pintu):
        super().__init__(nama, bensin)
        self.__jumlah_pintu = jumlah_pintu
 
    def get_jumlah_pintu(self):
        return self.__jumlah_pintu
 
    def set_jumlah_pintu(self, jumlah_pintu):
        self.__jumlah_pintu = jumlah_pintu
 
    def cek_bensin(self):
        if self.get_bensin() <= 0:
            print(f"{self.get_nama()}: Bensin mobil habis!")
        else:
            print(f"{self.get_nama()}: Bensin mobil masih tersedia.")
 
    def hitung_jarak_maksimal(self, liter_bensin, konsumsi_perliter):
        return liter_bensin * konsumsi_perliter * 0.9
 
 
class Motor(Kendaraan):
    def __init__(self, nama, bensin):
        super().__init__(nama, bensin)
 
    def cek_bensin(self, jarak_tempuh):
        if self.get_bensin() <= 0:
            print(f"{self.get_nama()}: Bensin motor habis!")
        elif jarak_tempuh > self.hitung_jarak_maksimal(1, 30):
            print(f"{self.get_nama()}: Jarak terlalu jauh, perlu isi bensin.")
        else:
            print(f"{self.get_nama()}: Bensin motor masih cukup.")
 
    def hitung_sisa_bensin(self, jarak_tempuh, konsumsi_perliter):
        self.set_bensin(self.get_bensin() - (jarak_tempuh / konsumsi_perliter))
        return self.get_bensin()
 
 
# Class baru untuk menampilkan deskripsi kendaraan
class InfoKendaraan:
    @staticmethod
    def tampilkan_info_kendaraan(kendaraan_list):
        i = 1
        for kendaraan in kendaraan_list:
            print(f"\n{i}.Info {kendaraan.get_nama()}:")
            print(f"Nama: {kendaraan.get_nama()}")
            print(f"Bensin: {kendaraan.get_bensin()} liter")
            print(f"Jumlah Pintu: {kendaraan.get_jumlah_pintu()}" if isinstance(kendaraan, Mobil) else "")
            i += 1
 
 
# Contoh penggunaan
mobil = Mobil("Mobil XYZ", 30, 4)
mobil.cek_bensin()
motor = Motor("Motor ABC", 10)
motor.cek_bensin(2000)
 
info_kendaraan = InfoKendaraan()
info_kendaraan.tampilkan_info_kendaraan([mobil, motor])