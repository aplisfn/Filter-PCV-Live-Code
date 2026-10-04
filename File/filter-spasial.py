
import cv2
import numpy as np


def filter_lowpass(citra):
    # 1. Box Filter
    hasil_box = cv2.blur(citra, (9, 9))

    # 2. Gaussian Filter
    hasil_gaussian = cv2.GaussianBlur(
        citra, (9, 9), sigmaX=2.0
    )

    # 3. Median Filter
    hasil_median = cv2.medianBlur(citra, 7)

    return hasil_box, hasil_gaussian, hasil_median


def filter_highpass(citra):
    citra_float = citra.astype(np.float32)

    # 4. Deteksi tepi Laplacian
    kernel_laplacian = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ], dtype=np.float32)

    hasil_lap = cv2.filter2D(
        citra_float, cv2.CV_32F, kernel_laplacian
    )
    hasil_lap = cv2.convertScaleAbs(hasil_lap)

    # 5. Unsharp Masking
    citra_blur = cv2.GaussianBlur(
        citra_float, (7, 7), sigmaX=2.0
    )

    detail = citra_float - citra_blur
    citra_tajam = citra_float + 2.0 * detail

    hasil_unsharp = np.clip(
        citra_tajam, 0, 255
    ).astype(np.uint8)

    # 6. Deteksi tepi Sobel
    grad_x = cv2.Sobel(
        citra_float, cv2.CV_32F, 1, 0, ksize=3
    )
    grad_y = cv2.Sobel(
        citra_float, cv2.CV_32F, 0, 1, ksize=3
    )

    magnitudo = cv2.magnitude(grad_x, grad_y)

    hasil_sobel = cv2.normalize(
        magnitudo,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    ).astype(np.uint8)

    return hasil_lap, hasil_unsharp, hasil_sobel


def tampilkan_gambar(judul, citra):
    cv2.imshow(judul, citra)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Membaca gambar asli berwarna
citra_warna = cv2.imread(
    "gambar.jpg", cv2.IMREAD_COLOR
)

if citra_warna is None:
    raise FileNotFoundError(
        "gambar.jpg tidak ditemukan. "
        "Pastikan file berada di folder yang sama."
    )

# Mengubah gambar menjadi grayscale untuk filtering
citra = cv2.cvtColor(
    citra_warna, cv2.COLOR_BGR2GRAY
)

# Menjalankan filter lowpass
box, gaussian, median = filter_lowpass(citra)

# Menjalankan filter highpass
laplacian, unsharp, sobel = filter_highpass(citra)

daftar_hasil = [
    ("1. Citra Asli Berwarna", citra_warna),
    ("2. Citra Grayscale", citra),
    ("3. Box Filter", box),
    ("4. Gaussian Filter", gaussian),
    ("5. Median Filter", median),
    ("6. Deteksi Tepi Laplacian", laplacian),
    ("7. Unsharp Masking", unsharp),
    ("8. Deteksi Tepi Sobel", sobel)
]


for judul, hasil in daftar_hasil:
    print("Menampilkan:", judul)
    tampilkan_gambar(judul, hasil)

print("Seluruh proses filtering selesai.")