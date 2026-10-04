
import cv2
import math
import numpy as np


def transformasi_intensitas(gambar):
    tinggi, lebar = gambar.shape

    hasil_negatif = np.zeros_like(gambar)
    hasil_log = np.zeros_like(gambar)
    hasil_gamma = np.zeros_like(gambar)

    # Membuat tabel transformasi intensitas
    tabel_log = []
    tabel_gamma = []

    konstanta_log = 255 / math.log(256)
    gamma = 0.5

    for i in range(256):
        nilai_log = konstanta_log * math.log(1 + i)
        tabel_log.append(int(nilai_log))

        nilai_gamma = 255 * ((i / 255) ** gamma)
        tabel_gamma.append(int(round(nilai_gamma)))

    # Mengubah intensitas setiap piksel secara manual
    for y in range(tinggi):
        for x in range(lebar):
            intensitas = int(gambar[y, x])

            hasil_negatif[y, x] = 255 - intensitas
            hasil_log[y, x] = tabel_log[intensitas]
            hasil_gamma[y, x] = tabel_gamma[intensitas]

    return hasil_negatif, hasil_log, hasil_gamma


def ekualisasi_histogram(gambar):
    tinggi, lebar = gambar.shape
    jumlah_piksel = tinggi * lebar

    # Menghitung frekuensi setiap intensitas
    histogram = [0] * 256

    for y in range(tinggi):
        for x in range(lebar):
            intensitas = int(gambar[y, x])
            histogram[intensitas] += 1

    # Menghitung distribusi kumulatif
    cdf = [0] * 256
    cdf[0] = histogram[0]

    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + histogram[i]

    # Mencari CDF minimum yang tidak bernilai nol
    cdf_min = 0
    for nilai in cdf:
        if nilai > 0:
            cdf_min = nilai
            break

    # Membuat pemetaan intensitas baru
    tabel_equal = [0] * 256
    penyebut = jumlah_piksel - cdf_min

    for i in range(256):
        if penyebut > 0:
            nilai_baru = 255 * (cdf[i] - cdf_min) / penyebut
            nilai_baru = max(0, min(255, nilai_baru))
            tabel_equal[i] = int(round(nilai_baru))
        else:
            tabel_equal[i] = i

    # Menerapkan hasil pemetaan ke gambar
    hasil = np.zeros_like(gambar)

    for y in range(tinggi):
        for x in range(lebar):
            intensitas = int(gambar[y, x])
            hasil[y, x] = tabel_equal[intensitas]

    return hasil


# Membaca gambar
nama_file = "gambar.jpg"
gambar = cv2.imread(nama_file, cv2.IMREAD_GRAYSCALE)

if gambar is None:
    raise FileNotFoundError(
        f"Gambar '{nama_file}' tidak ditemukan. Periksa lokasi file."
    )

# Menjalankan transformasi intensitas
negatif, logaritmik, gamma = transformasi_intensitas(gambar)

# Menjalankan ekualisasi histogram
hasil_equal = ekualisasi_histogram(gambar)

# Menampilkan hasil
hasil_gambar = [
    ("Gambar Asli", gambar),
    ("Transformasi Negatif", negatif),
    ("Transformasi Logaritmik", logaritmik),
    ("Transformasi Gamma 0.5", gamma),
    ("Ekualisasi Histogram", hasil_equal)
]

for judul, hasil in hasil_gambar:
    cv2.imshow(judul, hasil)

cv2.waitKey(0)
cv2.destroyAllWindows()