# Manualy Split Bill

## 📌 Deskripsi Proyek
Proyek ini dibuat untuk kamu kalo mau spllit bill dengan teman-teman mu secara manual. Mungkin memang terkesan jelek dan biasa saja tapi yang penting bisa berguna. Gak ada embel-embel AI dan Machine Learning pada proyek kali ini (sejenak rehat dari dunia sains data). Karena pada dasarnya proyek ini dibuat untuk melatih pemahaman alur algoritma dan pembuatan struktur data


## 🚀 Cara Menggunakan Program
### 1️⃣ **Download SplitBill.py**  
download file py yang tersedia kemudian letakan pada sebuah folder baru.

### 2️⃣ Instalasi Dependensi
Pastikan Python 3.8+ terinstal dan pastikan terdapat pandas v2.2.3++ pada env mu

### 3️⃣ Buat file ipynb baru kemudian import py tadi
buat file ipynb pada folder yang sama dengan letak file SplitBill.py tadi. kemudian import splitbill
```bash
from SplitBill import splitbill
```
### 4️⃣ Inisiasi program
pertama lakukan inisiasi class pada notebook kamu
```bash 
split_gacoan = splitbill()
split_gacoan.start_split()
```

### 5️⃣inputasi awal
- kamu akan ditanyakan akan melakukan splitbill dengan berapa orang (pastikan input berupa bilangan bulat)
- kamu diminta untuk memasukkan besar pajak (PPN) pada toko kamu berbelanja (input berupa float, jika PPN 10% cukup tulis 10, jika 10.5% tulis 10.5)

### 6️⃣ inputasi pesanan
pada bagian ini kamu diminta untuk melakukan:
- memasukan barang apa saja yang kamu pesan
- berapa kuantitas masing-masing barangnya
- berapa total bayar untuk masing-masing barangnya
- **!!!pastikan untuk ketik 'done' jika sudah semua barang kamu masukkan!!!**  

setelah proses ini selesai pada layar akan ditampilkan harga masing-masing barang setelah pajak

### 7️⃣ inputasi nama-nama orang
pada bagian ini kamu diminta untuk memasukan nama teman-teman mu pada program. pastikan untuk hit 'enter' untuk masing-masing anggota.

### 8️⃣ inputasi kuantitas pesanan per-orang
pada bagian ini kamu akan melakukan:
- memasukkan kuantitas barang yang dipesan untuk masing-orang
- kuantitas barang harus berupa integer dan tidak boleh lebih dari sisa barang yang tertera
- orang terakhir tidak perlu kamu lakukan inputasi kuantitas karena sudah pasti sisanya.  

(emg bagian ini paling lama dan malesin, namanya juga manual mau gimana bre)

### 9️⃣ Hasil Split Bill Kalian
Setelah semua langkah selesai di layar akan ditampilkan hasil dari split bill kalian. akan terdapat dua tampilan:
- rincian pesanan dari masing-masing teman mu dan total tagihan yang harus dibayarkan
- (hanya) total tagihan yang harus dibayarkan

terimakasih sudah ikut gabut bersama Jeepes!!

## 🚀 Target dan Harapan Pengengembangan
- membuat dan melatih arsitektur deep learning berbasis convulutional neural network ataupun melatih model machine learning tradisional untuk membaca script/struk belanja agar user tidak perlu secara manual menginput data pesanan
- membuat interface sederhana agar lebih ramah untuk banyak pengguna

## 👥 **Kontributor Utama**  
- **Dani Hidayat**  





