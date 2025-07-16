import cv2

#membuat model Haar Cascade untuk deteksi wajah
face_cascade = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#mengecek apakah dapat dimuat
if face_cascade.empty():
    print("gagal memuat model deteksi wajah")
    exit()

#membuka kamera
kameraSource = cv2.VideoCapture(0)

while True:
    ret, kamera = kameraSource.read()

    if not ret:
        break

    #mengubah ke grayscale sehingga dapat mendeteksi dengan cepat
    kameraAbu = cv2.cvtColor(kamera, cv2.COLOR_BGR2GRAY)

    #mendeteksi wajah dalam gambar
    faces = face_cascade.detectMultiScale(
        kameraAbu,
        scaleFactor=1.1,
        minNeighbors=5
    )

    #Jika wajah terdeteksi gambar kotak pada wajah
    for (x,y,w,h) in faces:
        cv2.rectangle(kamera, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(kamera, "wajah", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255,0), 2)

    #Menampilkan hasil dari kamera
    cv2.imshow("mendeteksi wajah", kamera)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#menutup kamera dan jendela
kameraSource.release()
cv2.destroyAllWindows()



