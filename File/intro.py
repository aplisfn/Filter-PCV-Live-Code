import cv2


# membaca file
image = cv2.imread("gambar.jpg")
imgtype = image.dtype
(h,w,c) = image.shape

#filter gambar
for i in range(w):
    for j in range(h):
        image[j,i,1] = 0
        image[j,i,0] = 0

# menampilkan image
cv2.imshow("Image", image)
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

    cv2.imshow("tes tugas pcv", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()