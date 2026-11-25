
import cv2
import numpy as np


def operasi_erosi(citra, kernel):
    hasil = cv2.erode(
        citra,
        kernel,
        iterations=1
    )
    return hasil


def operasi_dilasi(citra, kernel):
    hasil = cv2.dilate(
        citra,
        kernel,
        iterations=1
    )
    return hasil


def operasi_opening(citra, kernel):
    hasil = cv2.morphologyEx(
        citra,
        cv2.MORPH_OPEN,
        kernel
    )
    return hasil


def operasi_closing(citra, kernel):
    hasil = cv2.morphologyEx(
        citra,
        cv2.MORPH_CLOSE,
        kernel
    )
    return hasil


def tampilkan_gambar(judul, gambar):
    cv2.imshow(judul, gambar)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Membaca gambar asli
gambar = cv2.imread(
    "gambar.jpg",
    cv2.IMREAD_COLOR
)

if gambar is None:
    raise FileNotFoundError(
        "gambar.jpg tidak ditemukan. Periksa lokasi file."
    )


# Mengubah gambar menjadi grayscale
citra = cv2.cvtColor(
    gambar,
    cv2.COLOR_BGR2GRAY
)


# Membuat structuring element
kernel = np.ones(
    (5, 5),
    dtype=np.uint8
)


# Melakukan operasi morfologi
hasil_erosi = operasi_erosi(citra, kernel)
hasil_dilasi = operasi_dilasi(citra, kernel)
hasil_opening = operasi_opening(citra, kernel)
hasil_closing = operasi_closing(citra, kernel)


# Menyiapkan hasil untuk ditampilkan
daftar_hasil = [
    ("1. Gambar Asli", gambar),
    ("2. Grayscale", citra),
    ("3. Erosi", hasil_erosi),
    ("4. Dilasi", hasil_dilasi),
    ("5. Opening", hasil_opening),
    ("6. Closing", hasil_closing)
]


# Menampilkan hasil satu per satu
for judul, hasil in daftar_hasil:
    print("Menampilkan:", judul)
    tampilkan_gambar(judul, hasil)


print("Seluruh operasi morfologi selesai.")
