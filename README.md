Repositori ini berisi file tugas mata kuliah PCV

# 1. Filter-PCV-Live-Code

## File name : 
- intro.py
- Gambar.jpg

Code filter warna untuk pertemuan mata kuliah Pengolahan Citra dan Visi (PCV).

## Fitur

Program ini memiliki beberapa fungsi:

- Membaca file gambar menggunakan OpenCV
- Menampilkan gambar asli
- Melakukan filter warna merah pada gambar
- Melakukan filter warna hijau pada gambar
- Melakukan filter warna biru pada gambar
- Mengambil video secara langsung dari webcam
- Melakukan filter warna merah pada video secara real-time

## Requirements

Library yang digunakan:

- Python
- OpenCV

## NB :
Tekan tombol **ESC** untuk keluar dari program saat webcam sedang berjalan.


Install OpenCV dengan:

```bash
pip install opencv-python
```
# 2. Transformasi Intensitas dan Ekualisasi Histogram - PCV

Repository ini berisi implementasi transformasi intensitas dan ekualisasi histogram menggunakan Python dan OpenCV untuk tugas praktikum Pengolahan Citra dan Visi Komputer (PCV).

## Fitur

* Membaca dan menampilkan gambar asli berwarna.
* Mengubah gambar menjadi grayscale.
* Transformasi negatif untuk membalik intensitas piksel.
* Transformasi logaritmik untuk mengubah rentang intensitas gambar.
* Transformasi gamma dengan nilai gamma 0.5.
* Ekualisasi histogram untuk memperbaiki distribusi intensitas piksel.
* Menampilkan hasil pemrosesan gambar satu per satu.

## Requirements

Library yang digunakan:

* Python
* OpenCV (`opencv-python`)
* NumPy

Instalasi library:

```bash
pip install opencv-python numpy
```

## Struktur Folder

```text
PCV/
├── ti-eq.py
├── gambar.jpg
└── README.md
```

## Cara Menjalankan

1. Pastikan file `gambar.jpg` berada di folder yang sama dengan `ti-eq.py`.
2. Buka terminal pada folder tersebut.
3. Jalankan perintah berikut:

```bash
python 2-ti-eq.py
```

4. Hasil gambar akan ditampilkan secara berurutan.
5. Tutup jendela atau tekan tombol keyboard untuk melanjutkan ke hasil berikutnya.

## Metode yang Digunakan

### 1. Transformasi Negatif

Mengubah intensitas setiap piksel menggunakan rumus:

$$
s = 255-r
$$

### 2. Transformasi Logaritmik

Memperluas rentang intensitas pada bagian gambar yang memiliki nilai piksel rendah menggunakan rumus:

$$
s = \frac{255}{\ln(256)}\ln(1+r)
$$

### 3. Transformasi Gamma

Mengubah intensitas piksel menggunakan nilai gamma sebesar 0.5 dengan rumus:

$$
s = 255\left(\frac{r}{255}\right)^{0.5}
$$

### 4. Ekualisasi Histogram

Menghitung histogram dan distribusi kumulatif (*Cumulative Distribution Function* atau CDF) secara manual untuk memetakan intensitas piksel agar distribusi kontras gambar dapat diperbaiki.

## Catatan

* Transformasi intensitas dan ekualisasi histogram dihitung menggunakan perulangan dan tabel pemetaan intensitas secara manual.
* Program tidak menggunakan fungsi bawaan OpenCV untuk melakukan transformasi tersebut.
* Gambar asli ditampilkan dalam format berwarna, sedangkan hasil transformasi ditampilkan dalam grayscale.




