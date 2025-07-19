import cv2
import numpy as np

kameraSource = cv2.VideoCapture(0)


while True:
    ret, kamera = kameraSource.read()

    if not ret:
        break

    hsv = cv2.cvtColor(kamera, cv2.COLOR_BGR2HSV)

    # Rentang warna biru
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255,255])

    #Masking dan hasil dengan hsv
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    hasil_biru = cv2.bitwise_and(kamera, kamera, mask = mask_blue)

    # Deteksi Kontur
    contours, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:

            #gambar kontur
            cv2.drawContours(kamera, [cnt], 0, (0,255,0), 2)

            # bounding box
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(kamera, (x,y), (x+w, y+h), (255,0,0), 2)

            # teks
            cv2.putText(kamera, "Objek Berwarna Biru", (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

    # tampilkan hasil
    cv2.imshow("Kamera", kamera)
    cv2.imshow("Mask", mask_blue)
    cv2.imshow("hasil", hasil_biru)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

kameraSource.release()
cv2.destroyAllWindows()
            
