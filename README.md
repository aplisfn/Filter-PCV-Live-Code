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
# 2. Transformasi Intensitas dan Ekualisasi Histogram 

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

# 3. Spatial Filtering 

Program ini merupakan implementasi filter spasial pada citra digital menggunakan Python, OpenCV, dan NumPy. Filter spasial digunakan untuk menghaluskan citra, mengurangi noise, mempertajam detail, dan mendeteksi tepi.

## Fitur

* Membaca dan menampilkan citra asli berwarna.
* Mengubah citra berwarna menjadi grayscale.
* Menerapkan Box Filter.
* Menerapkan Gaussian Filter.
* Menerapkan Median Filter.
* Mendeteksi tepi menggunakan Laplacian.
* Mempertajam citra menggunakan Unsharp Masking.
* Mendeteksi tepi menggunakan Sobel.
* Menampilkan hasil pemrosesan satu per satu.

## Requirements

Library yang digunakan:

* Python
* OpenCV
* NumPy

Instalasi library:

```bash
pip install opencv-python numpy
```

## Struktur Folder

```text
PCV/
├── filter-spasial.py
├── gambar.jpg
└── README.md
```

## Cara Menjalankan

1. Pastikan file `gambar.jpg` berada di folder yang sama dengan program.
2. Buka terminal pada folder tugas.
3. Jalankan perintah berikut:

```bash
python 3-filter-spasial.py
```

4. Program akan menampilkan citra asli berwarna, citra grayscale, dan hasil setiap filter secara berurutan.
5. Tutup jendela gambar atau tekan tombol keyboard untuk melanjutkan ke hasil berikutnya.

## Metode yang Digunakan

### 1. Box Filter

Menghaluskan citra dengan mengganti nilai setiap piksel menggunakan rata-rata piksel di sekitarnya. Pada program ini digunakan kernel berukuran 9 × 9.

### 2. Gaussian Filter

Menghaluskan citra menggunakan distribusi Gaussian sehingga piksel yang lebih dekat dengan pusat kernel memiliki bobot lebih besar.

### 3. Median Filter

Mengurangi noise dengan mengganti nilai piksel menggunakan median dari lingkungan sekitarnya.

### 4. Laplacian Filter

Mendeteksi perubahan intensitas piksel untuk menonjolkan tepi dan detail citra. Hasil yang ditampilkan berupa respons tepi dalam skala grayscale.

### 5. Unsharp Masking

Mempertajam citra dengan menambahkan detail yang diperoleh dari selisih citra asli dan citra yang telah dihaluskan.

### 6. Sobel Filter

Mendeteksi tepi dengan menghitung gradien intensitas dalam arah horizontal dan vertikal, kemudian menggabungkan keduanya untuk menghasilkan magnitudo gradien.

## Catatan

* Citra asli ditampilkan dalam format berwarna.
* Proses filtering dilakukan pada citra grayscale.
* Ukuran kernel memengaruhi tingkat penghalusan dan detail yang dihasilkan.
* Hasil setiap filter ditampilkan secara berurutan agar dapat dibandingkan dengan citra asli.




