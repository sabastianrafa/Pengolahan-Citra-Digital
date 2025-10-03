# melakukan import liblary cv2 (Computer Vision) yang digunakan untuk manipulasi gambar sederhana sampai pemrosesan video dan machine learning
import cv2

# mengambil gambar
image = cv2.imread(".\GUA.png")

# Resize jadi 300 x 300
resized_image = cv2.resize(image, (300, 300))

# mengubah gambar menjai gray
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# ubah menjadi biner (thresholding)
_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
# 128 = nilai ambang (bisa disesuaikan), 
# pixel > 128 → 255 (putih), pixel <= 128 → 0 (hitam)

# menampilkan gambar asli
cv2.imshow("Gambar Asli", resized_image)
# menampilkan gambar yang sudah di ubah
cv2.imshow("Gambar", gray_image)
# menampilkan gambar biner
cv2.imshow("Biner", binary_image)
# waktu tunggu untuk menampilkan gambar dalam milidetik, 
# 0 berati menunggu selamanya sampai tombol x di tekan
cv2.waitKey(0)