import cv2 
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

# Resimdeki yüzleri algılama işlevi
def detect_faces_from_image(image_path):
    # Kedi yüzü algılama için Haar cascade dosyasını yükle
    cat_face_cascade = cv2.CascadeClassifier('haarcascade dosyasının yolunu giriniz')

    # İnsan yüzü algılama için Haar cascade dosyasını yükle
    human_face_cascade = cv2.CascadeClassifier('haarcascade dosyasının yolunu giriniz')

    # Köpek yüzü algılama için Haar cascade dosyasını yükle
    dog_face_cascade = cv2.CascadeClassifier('haarcascade dosyasının yolunu giriniz')

    # Resmi yükle
    img = cv2.imread(image_path)

    # Hedef boyut
    target_size = (500, 700)

    # Resmi hedef boyuta boyutlandır
    img = cv2.resize(img, target_size, interpolation=cv2.INTER_AREA)

    # Gri tonlamaya dönüştür
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Kedi yüzlerini algıla
    cat_faces = cat_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20))

    # İnsan yüzlerini algıla
    human_faces = human_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=20, minSize=(30, 30))

    # Köpek yüzlerini algıla
    dog_faces = dog_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(20, 20))

    # Eğer yüz algılanamadıysa
    if len(cat_faces) == 0 and len(human_faces) == 0 and len(dog_faces) == 0:
        messagebox.showinfo("Bilgilendirme", "Yüz bulunamadı. Bu program henüz gelişim aşamasında bu nedenle yüklediğiniz görseli algılayamamış olabilir anlayışınız için teşekkürler.")
        return

    # Algılanan kedi yüzlerini işle
    for (x, y, w, h) in cat_faces:
        # Yüzü çerçeve içine al
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 5)
        # Yüzün kedi olduğunu belirle
        cv2.putText(img, "Kedi", (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (125, 0, 0), 2)

    # Algılanan insan yüzlerini işle
    for (x, y, w, h) in human_faces:
        # Yüzü çerçeve içine al
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 5)
        # Yüzün insan olduğunu belirle
        cv2.putText(img, "Insan", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (36,255,12), 4)

    # Algılanan köpek yüzlerini işle
    for (x, y, w, h) in dog_faces:
        # Yüzü çerçeve içine al
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 5)
        # Yüzün köpek olduğunu belirle
        cv2.putText(img, "Kopek", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (36,255,255), 4)

    # Sonuçları göster
    cv2.imshow('Sonuclar', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Resim seçme işlevi
def select_image():
    image_path = filedialog.askopenfilename()  # Kullanıcıya dosya seçme penceresi gösterir ve seçilen dosyanın yolunu döndürür
    detect_faces_from_image(image_path)

# Kamera görüntüsünden yüz algılama işlevi
def detect_faces_from_camera():
    # Kedi yüzü algılama için Haar cascade dosyasını yükle
    cat_face_cascade = cv2.CascadeClassifier('haarcascade dosyasının yolunu giriniz')

    # İnsan yüzü algılama için Haar cascade dosyasını yükle
    human_face_cascade = cv2.CascadeClassifier('haarcascade dosyasının yolunu giriniz')

    # Köpek yüzü algılama için Haar cascade dosyasını yükle
    dog_face_cascade = cv2.CascadeClassifier('haarcascade dosyasının yolunu giriniz')

    # Kamera aç
    cap = cv2.VideoCapture(0)

    while True:
        # Kameradan görüntü al
        ret, frame = cap.read()

        # Gri tonlamaya dönüştür
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Kedi yüzlerini algıla
        cat_faces = cat_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20))

        # İnsan yüzlerini algıla
        human_faces = human_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15, minSize=(30, 30))

        # Köpek yüzlerini algıla
        dog_faces = dog_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=13, minSize=(30, 30))

        # Algılanan yüzleri işle
        for (x, y, w, h) in cat_faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)  # Kedi yüzlerini çerçeve içine al
            cv2.putText(frame, "Kedi", (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (125, 0, 0), 2)  # Yüzün kedi olduğunu belirle
        for (x, y, w, h) in human_faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)  # İnsan yüzlerini çerçeve içine al
            cv2.putText(frame, "Insan", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (36,255,12), 4)  # Yüzün insan olduğunu belirle
        for (x, y, w, h) in dog_faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 5)  # Köpek yüzlerini çerçeve içine al
            cv2.putText(frame, "Köpek", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (36,255,255), 4)  # Yüzün köpek olduğunu belirle

        # Sonuçları göster
        cv2.imshow('Sonuclar', frame)

        # Çıkış için 'q' tuşuna bas
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Pencereyi kapat
    cap.release()
    cv2.destroyAllWindows()


# Tkinter penceresi oluştur
root = tk.Tk()
root.title("Yüz Algılama")
root.geometry("800x600")  # Pencere boyutunu belirle

# Resim seçme düğmesi
button_select = tk.Button(root, text="Resim Seç", command=select_image)  # Resim seçme işlevini başlatan düğme
button_select.pack()  # Düğmeyi ekrana yerleştir

# Kamera görüntüsünü işlemeye yarayan düğme
button_detect_camera = tk.Button(root, text="Kameradan Görüntü Al ve Algıla", command=detect_faces_from_camera)  # Kameradan görüntü alıp yüzleri algılama işlevini başlatan düğme
button_detect_camera.pack()  # Düğmeyi ekrana yerleştir


# Pencereyi aç
root.mainloop()  # Tkinter penceresini başlat ve olay döngüsünü başlat


