import cv2

kameraSource = cv2.VideoCapture(0)

while True:
	ret, bukaKamera = kameraSource.read()
	
	if not ret:
		break
		
	grayscale = cv2.cvtColor(bukaKamera, cv2.COLOR_BGR2GRAY)
	tepi = cv2.Canny (grayscale, 50, 150)
	
	cv2.imshow('kamera origin', bukaKamera)
	cv2.imshow('kamera abu abu', grayscale)
	cv2.imshow('kamera tepi', tepi)
	
	if cv2.waitKey(1) & 0xFF == ord ('q'):
		break
	
cap.release()
cv2.destroyAllWindows()
