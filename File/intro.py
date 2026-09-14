import cv2


# membaca file
image = cv2.imread("gambar.jpg")
imgtype = image.dtype
(h, w, c) = image.shape

imgMerah = image.copy()
imgHijau = image.copy()
imgBiru = image.copy()


# filter gambar
for i in range(w):
    for j in range(h):

        # Filter merah
        imgMerah[j, i, 0] = 0
        imgMerah[j, i, 1] = 0

        # Filter hijau
        imgHijau[j, i, 0] = 0
        imgHijau[j, i, 2] = 0

        # Filter biru
        imgBiru[j, i, 1] = 0
        imgBiru[j, i, 2] = 0


# Menampilkan gambar asli
cv2.imshow("Image Asli", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Menampilkan filter gambar merah
cv2.imshow("Image Filter Warna Merah", imgMerah)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Menampilkan filter gambar hijau
cv2.imshow("Image Filter Warna Hijau", imgHijau)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Menampilkan filter gambar biru
cv2.imshow("Image Filter Warna Biru", imgBiru)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Filter color video (live cam webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    h, w, c = frame.shape

    for i in range(h):
        for j in range(w):
            frame[i,j,1] = 0
            frame[i,j,0] = 0

    cv2.imshow("Filter Merah Video Capture", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()