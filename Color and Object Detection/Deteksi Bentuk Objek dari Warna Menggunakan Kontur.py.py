import cv2
import numpy as np

kameraSource = cv2.VideoCapture(0)

while True:
    ret, kamera = kameraSource.read()

    if not ret:
        break

    hsv = cv2.cvtColor(kamera, cv2.COLOR_BGR2HSV)

    # Mengambil sampel warna orange
    lower_orange = np.array([10, 100, 100])
    upper_orange = np.array([25, 255, 255])

    # Membuat mask
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    
    # Menghaluskan Mask
    mask = cv2.GaussianBlur(mask, (7,7), 0)

    # Menemukan kontur
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        #melewati contours kecil
        if cv2.contourArea(cnt) < 1000:
            continue

        # Mengambil gambar kontur
        approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
        x,y,w,h = cv2.boundingRect(approx)

        # Deteksi bentuk
        bentuk = "tidak diketahui"
        sisi = len(approx)

        if sisi == 3:
            bentuk = "segitiga"

        elif sisi == 4:
            bentuk = "persegi"

        elif sisi > 4:
            bentuk = "lingkaran"
        
        # Gambar kotak dan teks
        cv2.drawContours(kamera, [approx], 0, (0, 255, 0), 3)
        cv2.putText(kamera, bentuk, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # Tampilkan hasil
    cv2.imshow("Deteksi Bentuk Objek dari Warna", kamera)
    cv2.imshow("Mask", mask)

    # Tombol ESC untuk keluar
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

kameraSource.release()
cv2.destroyAllWindows()
