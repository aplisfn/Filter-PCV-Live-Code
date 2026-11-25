import cv2
import numpy as np
import math


def konversi_cmyk(rgb):
    # Normalisasi nilai RGB ke rentang 0-1
    rgb = rgb.astype(np.float32) / 255.0

    r = rgb[:, :, 0]
    g = rgb[:, :, 1]
    b = rgb[:, :, 2]

    # Menghitung komponen CMYK
    k = 1 - np.maximum.reduce([r, g, b])

    penyebut = 1 - k

    c = np.zeros_like(k)
    m = np.zeros_like(k)
    y = np.zeros_like(k)

    valid = penyebut > 0

    c[valid] = (1 - r[valid] - k[valid]) / penyebut[valid]
    m[valid] = (1 - g[valid] - k[valid]) / penyebut[valid]
    y[valid] = (1 - b[valid] - k[valid]) / penyebut[valid]

    return (
        (c * 255).astype(np.uint8),
        (m * 255).astype(np.uint8),
        (y * 255).astype(np.uint8),
        (k * 255).astype(np.uint8)
    )


def konversi_hsi(rgb):
    # Normalisasi RGB
    data = rgb.astype(np.float32) / 255.0

    r = data[:, :, 0]
    g = data[:, :, 1]
    b = data[:, :, 2]

    # Menghitung Hue
    pembilang = 0.5 * ((r - g) + (r - b))

    penyebut = np.sqrt(
        (r - g) ** 2 + (r - b) * (g - b)
    )

    theta = np.arccos(
        np.clip(
            pembilang / (penyebut + 1e-10),
            -1, 1
        )
    )

    hue = np.where(b <= g, theta, 2 * np.pi - theta)
    hue = np.degrees(hue)

    # Menghitung Saturation
    jumlah = r + g + b
    minimum = np.minimum.reduce([r, g, b])

    saturation = np.zeros_like(r)
    valid = jumlah > 0

    saturation[valid] = (
        1 - (3 * minimum[valid] / jumlah[valid])
    )

    # Menghitung Intensity
    intensity = jumlah / 3

    # Mengubah komponen menjadi citra 8-bit
    h = (hue / 360 * 255).astype(np.uint8)
    s = (saturation * 255).astype(np.uint8)
    i = (intensity * 255).astype(np.uint8)

    return h, s, i


def konversi_hsv(rgb):
    # OpenCV menggunakan rentang Hue 0-179
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)

    hue = hsv[:, :, 0]
    saturation = hsv[:, :, 1]
    value = hsv[:, :, 2]

    return hue, saturation, value


def tampilkan(judul, gambar):
    cv2.imshow(judul, gambar)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Membaca gambar berwarna
gambar = cv2.imread("gambar.jpg", cv2.IMREAD_COLOR)

if gambar is None:
    raise FileNotFoundError(
        "gambar.jpg tidak ditemukan. Periksa lokasi file."
    )

# Mengubah format BGR menjadi RGB
rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)

# Konversi ke CMYK
cyan, magenta, yellow, black = konversi_cmyk(rgb)

# Konversi ke HSI
h_hsi, s_hsi, i_hsi = konversi_hsi(rgb)

# Konversi ke HSV
h_hsv, s_hsv, v_hsv = konversi_hsv(rgb)


# Menyiapkan seluruh hasil konversi
daftar_hasil = [
    ("1. Gambar Asli RGB", cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)),

    ("2. RGB - Red", rgb[:, :, 0]),
    ("3. RGB - Green", rgb[:, :, 1]),
    ("4. RGB - Blue", rgb[:, :, 2]),

    ("5. CMYK - Cyan", cyan),
    ("6. CMYK - Magenta", magenta),
    ("7. CMYK - Yellow", yellow),
    ("8. CMYK - Black", black),

    ("9. HSI - Hue", h_hsi),
    ("10. HSI - Saturation", s_hsi),
    ("11. HSI - Intensity", i_hsi),

    ("12. HSV - Hue", h_hsv),
    ("13. HSV - Saturation", s_hsv),
    ("14. HSV - Value", v_hsv)
]


# Menampilkan hasil satu per satu
for judul, hasil in daftar_hasil:
    print("Menampilkan:", judul)
    tampilkan(judul, hasil)

print("Seluruh konversi model warna selesai.")
