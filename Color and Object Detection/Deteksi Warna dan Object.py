import cv2
import numpy as np

kameraSource = cv2.VideoCapture(0)

while True:
    ret, kamera = kameraSource.read()

    if not ret:
        break

    #mengubah HSV / Deteksi Warna
    hsv = cv2.cvtColor(kamera, cv2.COLOR_BGR2HSV)

    #menerapkan HSV batas masing - masing warna
    lower_orange = np.array([10, 100, 100])
    uppuer_orange = np.array([25, 255, 255])

    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255,255])

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255,255])

    upper_green = np.array([36, 100, 100])
    lower_green = np.array([86, 255, 255])

    #membuat masking warna (bagian yang terdeteksi berwarna = putih)
    mask_orange = cv2.inRange(hsv, lower_orange, uppuer_orange)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    #menggabungkan mask dengan gambar asli
    hasil_orange = cv2.bitwise_and(kamera, kamera, mask = mask_orange)
    hasil_biru = cv2.bitwise_and(kamera, kamera, mask = mask_blue)
    hasil_red = cv2.bitwise_and(kamera, kamera, mask = mask_red)
    hasil_green = cv2.bitwise_and(kamera, kamera, mask = mask_green)


    def deteksi_warna(mask, hasil, label, warna_bgr):
        kontur, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in kontur:
            area = cv2.contourArea(cnt)
            if area > 500:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(hasil, (x, y), (x + w, y + h), warna_bgr, 2)
                cv2.putText(hasil, label, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, warna_bgr, 2, cv2.LINE_AA)

    #tampilkan hasil kamera orginal
    cv2.imshow('Kamera Origin', kamera)

    #tampilkan hasil kamera mask
    cv2.imshow('Mask Orange', mask_orange)
    cv2.imshow('Mask Biru', mask_blue)
    cv2.imshow('Mask Merah', mask_red)
    cv2.imshow('Mask Hijau', mask_green)

    #Tampilkan deteksi warna
    deteksi_warna(mask_orange, hasil_orange, "ORANGE", (0, 140, 255))
    deteksi_warna(mask_blue, hasil_biru, "BIRU", (255, 0, 0))
    deteksi_warna(mask_red, hasil_red, "MERAH", (0, 0, 255))
    deteksi_warna(mask_green, hasil_green, "HIJAU", (0, 255, 0))


    #tampilkan hasil
    cv2.imshow("Hasil Biru", hasil_biru)
    cv2.imshow('Hasil Orange', hasil_orange)
    cv2.imshow('Hasil Merah', hasil_red)
    cv2.imshow('Hasil Hijau', hasil_green)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kameraSource.release()
cv2.destroyAllWindows()