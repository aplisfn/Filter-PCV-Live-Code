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

# 4. Model Warna

Program ini merupakan implementasi konversi model warna menggunakan Python, OpenCV, dan NumPy. Konversi model warna dilakukan untuk mempelajari representasi warna dalam beberapa ruang warna, yaitu RGB, CMYK, HSI, dan HSV.

## Fitur

* Membaca dan menampilkan gambar asli berwarna.
* Memisahkan komponen warna RGB (Red, Green, Blue).
* Mengonversi RGB menjadi CMYK (Cyan, Magenta, Yellow, Black).
* Mengonversi RGB menjadi HSI (Hue, Saturation, Intensity).
* Mengonversi RGB menjadi HSV (Hue, Saturation, Value).
* Menampilkan setiap komponen model warna secara terpisah.
* Menampilkan hasil konversi satu per satu.

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
├── 4-model-warna.py
├── gambar.jpg
└── README.md
```

## Cara Menjalankan

1. Pastikan file `gambar.jpg` berada di folder yang sama dengan `4-model-warna.py`.
2. Buka terminal pada folder tugas.
3. Jalankan perintah berikut:

```bash
python 4-model-warna.py
```

4. Program akan menampilkan gambar asli dan setiap komponen model warna secara berurutan.
5. Tutup jendela gambar atau tekan tombol keyboard untuk melanjutkan ke hasil berikutnya.

## Metode yang Digunakan

### 1. RGB (Red, Green, Blue)

Model warna yang menggunakan tiga komponen utama, yaitu merah, hijau, dan biru. RGB merupakan model warna aditif yang menggabungkan ketiga warna untuk menghasilkan berbagai warna lainnya.

### 2. CMYK (Cyan, Magenta, Yellow, Black)

Model warna yang terdiri dari empat komponen, yaitu Cyan, Magenta, Yellow, dan Black. CMYK merupakan model warna subtraktif yang umum digunakan dalam proses pencetakan.

### 3. HSI (Hue, Saturation, Intensity)

Model warna yang memisahkan informasi warna menjadi tiga komponen. Hue menunjukkan jenis warna, Saturation menunjukkan tingkat kejenuhan warna, sedangkan Intensity menunjukkan intensitas atau kecerahan warna.

### 4. HSV (Hue, Saturation, Value)

Model warna yang terdiri dari Hue, Saturation, dan Value. Hue menunjukkan jenis warna, Saturation menunjukkan tingkat kejenuhan, sedangkan Value menunjukkan tingkat kecerahan warna.

## Catatan

* Gambar asli dibaca dalam format BGR dan dikonversi menjadi RGB sebelum proses konversi model warna.
* Perhitungan komponen CMYK dan HSI dilakukan menggunakan rumus secara manual.
* Konversi HSV menggunakan fungsi `cv2.cvtColor()` dari OpenCV.
* Setiap komponen warna ditampilkan dalam bentuk citra grayscale untuk memperlihatkan distribusi nilai masing-masing kanal.

---

# 5. Morphological Operations

Program ini merupakan implementasi operasi morfologi pada citra digital menggunakan Python, OpenCV, dan NumPy. Operasi morfologi digunakan untuk mengolah bentuk dan struktur objek pada citra berdasarkan elemen penstruktur (*structuring element*).

## Fitur

* Membaca dan menampilkan gambar asli berwarna.
* Mengubah gambar menjadi grayscale.
* Menerapkan operasi Erosi (Erosion).
* Menerapkan operasi Dilasi (Dilation).
* Menerapkan operasi Opening.
* Menerapkan operasi Closing.
* Menggunakan kernel berukuran 5 × 5 sebagai elemen penstruktur.
* Menampilkan hasil operasi morfologi satu per satu.

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
├── 5-morphology.py
├── gambar.jpg
└── README.md
```

## Cara Menjalankan

1. Pastikan file `gambar.jpg` berada di folder yang sama dengan `5-morphology.py`.
2. Buka terminal pada folder tugas.
3. Jalankan perintah berikut:

```bash
python 5-morphology.py
```

4. Program akan menampilkan gambar asli berwarna, gambar grayscale, dan hasil setiap operasi morfologi secara berurutan.
5. Tutup jendela gambar atau tekan tombol keyboard untuk melanjutkan ke hasil berikutnya.

## Metode yang Digunakan

### 1. Erosi (Erosion)

Erosi merupakan operasi morfologi yang digunakan untuk memperkecil area objek yang memiliki intensitas lebih terang. Operasi ini dilakukan dengan mengambil nilai minimum dari area piksel sesuai dengan elemen penstruktur.

### 2. Dilasi (Dilation)

Dilasi merupakan operasi morfologi yang digunakan untuk memperbesar area objek yang memiliki intensitas lebih terang. Operasi ini dilakukan dengan mengambil nilai maksimum dari area piksel sesuai dengan elemen penstruktur.

### 3. Opening

Opening merupakan kombinasi operasi erosi yang dilanjutkan dengan dilasi. Operasi ini digunakan untuk menghilangkan noise atau objek kecil yang tidak diinginkan tanpa mengubah bentuk utama objek secara signifikan.

### 4. Closing

Closing merupakan kombinasi operasi dilasi yang dilanjutkan dengan erosi. Operasi ini digunakan untuk menutup lubang kecil dan celah pada objek dalam citra.

## Catatan

* Citra asli ditampilkan dalam format berwarna.
* Proses operasi morfologi dilakukan pada citra grayscale.
* Elemen penstruktur yang digunakan berupa kernel berukuran 5 × 5.
* Setiap operasi menggunakan satu iterasi.
* Hasil operasi ditampilkan secara berurutan agar perubahan bentuk objek dapat diamati dan dibandingkan dengan citra asli.




