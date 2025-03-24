import pandas as pd

class splitbill:
    def __init__(self):
        self.harga_total = None
        self.jumlah_anggota = int(input("kamu mau split bill dengan berapa orang?").strip())
        self.pajak = float(input("berapa persen PPN di tempat tersebut? (jika PPN 10% cukup tulis 10, jika 10.5% tulis 10.5)").strip())/100
        self.data_pesanan = {"pesanan" :  [],
                            "kuantitas" : [],
                            "harga total" : []}
        self.harga_satuan = {}
        self.anggota = []
        self.data_pemesan = {}
        self.bayar_akhir = {}
        self.df_pesanan = None
        self.df_pemesan = None
        self.sisa_barang = {}
        self.rinci = {}

    # def input_awal(self):
    #     while True:
    #         try:
    #             jumlah_anggota = int(input("kamu mau split bill dengan berapa orang?").strip())
    #             break
    #         except ValueError:
    #             print(f"jumlah orang harus berupa bilangan bulat!")
    #     while True:
    #         try:
    #             pajak = float(input("berapa persen PPN di tempat tersebut? (jika PPN 10% cukup tulis 10, jika 10.5% tulis 10.5)").strip())/100
    #             break
    #         except ValueError:
    #             print(f"nilai pajak harus berupa angka tanpa simbol apapun kecuali koma '.'")
    #     self.jumlah_anggota = jumlah_anggota
    #     self.pajak = pajak

    def input_pesanan(self):
        n=0
        while True:
            psn = str(input(f"Nama Pesanan ke-{n+1} (ketik 'Done' jika sudah diinput semua): ").strip()).lower()
            if psn.lower() == "done":
                break  # Jika input benar, keluar dari loop
            while True:
                try:
                    qtt = int(input(f"Masukkan Jumlah Pesanan {psn}: ").strip())
                    break
                except ValueError:
                    print('jumlah pesanan harus berupa bilangan bulat!')
            while True:
                try:
                    bayar = float(input(f"Masukan Jumlah Tagihan untuk Pesanan {psn}: ").strip())
                    break
                except ValueError:
                    print('jumlah tagihan harus berupa angka')
            
            self.data_pesanan['pesanan'].append(psn)
            self.data_pesanan['kuantitas'].append(qtt)
            self.data_pesanan['harga total'].append(bayar)
            self.sisa_barang[psn] = qtt
            self.harga_total = sum(self.data_pesanan['harga total'])
            n += 1
        self.df_pesanan = pd.DataFrame(self.data_pesanan)

    def input_anggota(self):
        n = 0
        while True:
            if n == self.jumlah_anggota:
                break
            orang = str(input(f"masukan nama anggota ke-{n+1}").strip())
            n += 1
            if orang.lower() == "done":
                break
            self.anggota.append(orang)
            self.bayar_akhir[orang] = 0
    
    def input_pemesan(self):
        self.data_pemesan = {"Anggota": self.anggota}
        for i in self.data_pesanan['pesanan']:
            self.data_pemesan[i] = []
        for orang in self.data_pemesan["Anggota"]:
            if orang == self.data_pemesan["Anggota"][-1]:
                for barang in self.sisa_barang:
                    self.data_pemesan[barang].append(self.sisa_barang[barang])
                    self.sisa_barang[barang] += -self.sisa_barang[barang]
            else:
                for barang in self.sisa_barang:
                    if self.sisa_barang[barang] == 0:
                        self.data_pemesan[barang].append(0)
                    if self.sisa_barang[barang] > 0:
                        while True:
                            try:
                                qtt = int(input(f"{orang} pesen berapa {barang}? (sisa {self.sisa_barang[barang]} yang belum terdata): ").strip())
                                break
                            except ValueError:
                                print('jumlah pesanan harus berupa bilangan bulat!')
                        self.data_pemesan[barang].append(qtt)
                        self.sisa_barang[barang] += -qtt

        self.df_pemesan = pd.DataFrame(self.data_pemesan)

    def int_to_Rp(self, intr):
        angka = list(str(int(intr)))
        pnjg = len(angka)
        cek = 0

        for i in range(-1, -pnjg-1, -1):
            if i != -pnjg and i%3 == 0:
                angka.insert(i-cek,'.')
                cek += 1
        angka = "".join(angka)

        return "Rp"+angka

    def hitung_harga_satuan(self):
        self.harga_satuan = {i:0 for i in self.data_pesanan['pesanan']}

        for produk in self.harga_satuan:
            harga = self.df_pesanan[self.df_pesanan['pesanan'] == produk].iloc[0, 2] / self.df_pesanan[self.df_pesanan['pesanan'] == produk].iloc[0, 1]
            PPajak = harga + harga*self.pajak
            self.harga_satuan[produk] += int(PPajak)
        self.print_Rapih(self.harga_satuan)

    def print_Rapih(self, objek=None):
        if not objek:
            objek = self.bayar_akhir
        cek = max([len(i) for i in objek])+1
        for i in objek:
            bayar = self.int_to_Rp(objek[i])
            print(f"- {i + ' '*(cek - len(i))}: {bayar}")
        if objek == self.bayar_akhir:
            print(f"\nTotal: {self.int_to_Rp(sum(objek.values()))}")

    def input_bayar_akhir(self):
        for cust in self.data_pemesan['Anggota']:
            data_cust = self.df_pemesan[self.df_pemesan['Anggota'] == cust].reset_index(drop=True)
            for produk in data_cust.columns[1:]:
                if data_cust.loc[0, produk] != 0:
                    self.bayar_akhir[cust] += float(data_cust.loc[0, produk]*self.harga_satuan[produk])
        self.bayar_akhir = {i:int(self.bayar_akhir[i]) for i in self.bayar_akhir}
        self.bayar_akhir = dict(sorted(self.bayar_akhir.items(), key=lambda item: item[1], reverse=True))
    
    def rincian(self):
        self.rinci = {i:{} for i in self.df_pemesan['Anggota']}
        for orang in range(self.df_pemesan.shape[0]):
            for barang in range(1, self.df_pemesan.shape[1]):
                if int(self.df_pemesan.iloc[orang, barang]) > 0:
                    self.rinci[list(self.rinci.keys())[orang]][self.df_pemesan.columns[barang]] = int(self.df_pemesan.iloc[orang, barang])
            self.rinci[list(self.rinci.keys())[orang]]["total"] = self.bayar_akhir[list(self.rinci.keys())[orang]]
        self.rinci = dict(sorted(self.rinci.items(), key=lambda item: item[1]['total'], reverse=True))

        for orang in self.rinci:
            print(f"Rincian {orang}:")
            cek = max([len(i) for i in list(self.rinci[orang].keys())][:-1]) + 1
            for barang in list(self.rinci[orang].keys())[:-1]:
                print(f" - {barang + ' '*(cek - len(barang))}: {self.rinci[orang][barang]}")
            print(f"total bayar si {orang}: {self.int_to_Rp(self.rinci[orang]['total'])}\n")

    def start_split(self):
        print(f"pertama-tama kamu harus melakukan:\n- memasukan barang apa saja yang kamu pesan\n- berapa kuantitas masing-masing barangnya\n- berapa total bayar untuk masing-masing barangnya\n!!!ketik 'done' jika sudah semua barang kamu masukkan!!!")
        self.input_pesanan()
        print(f"\nberikut adalah harga satuan masing-masing barang setelah pajak!")
        self.hitung_harga_satuan()
        print(f"\nselanjutnya kamu harus memasukkan nama-nama temanmu!")
        self.input_anggota()
        print(f"\nmasukkan quantitas barang yang dipesan oleh masing-masing temanmu!")
        self.input_pemesan()
        print(f"\nberikut adalah hasil split bill kalian!!")
        self.input_bayar_akhir()
        self.rincian()
        print(f"\npake ini kalo mau lebih gampang screenshot!!")
        self.print_Rapih()
        print(f"\nTerimakasih sudah menggunakan program saya 😉. kritik dan saran langsung ke IG aja @danihdyt_")