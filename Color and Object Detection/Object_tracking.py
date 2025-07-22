import cv2
import numpy as np

kameraSource = cv2.VideoCapture(0)

while True:
    ret, kamera = kameraSource.read()
    
    if not ret:
        break

    hsv = cv2.cvtColor(kamera, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([10, 100, 100])
    upper_orange = np.array([25, 255, 255])

    mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
    mask_orange = cv2.GaussianBlur(mask_orange, (7,7), 0)

    hasil_orange = cv2.bitwise_and(kamera, kamera, mask = mask_orange)

    contours, _ = cv2.findContours(mask_orange,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) < 1000:
            continue

        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(kamera, (cx, cy), 10, (0, 255, 255), -1)
            cv2.putText(kamera, "Objek", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.imshow("Pelacakan Objek", kamera)
    cv2.imshow("Mask", mask_orange)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

kameraSource.release()
cv2.destroyAllWindows()
