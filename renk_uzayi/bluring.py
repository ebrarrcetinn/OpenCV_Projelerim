import cv2

# OpenCV ile resmi oku
image = cv2.imread("resimler/manzara2.jpg")

kernel_sizes = [(3, 3), (9, 9), (15, 15)]

for (kX, kY) in kernel_sizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow(f"Average Blur ({kX}x{kY})", blurred)

# Gauss bulanıklaştırma (OpenCV kullanarak)
gaussian = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow("Gaussian Blur (15x15)", gaussian)
median = cv2.medianBlur(image, 7)
# Bilateral (çift taraflı) filtre uygula
bilateral = cv2.bilateralFilter(
    src=image,        # Giriş görüntüsü
    d=9,              # Komşuluk çapı (pencere boyutu)
    sigmaColor=75,    # Renk benzerliği toleransı
    sigmaSpace=75     # Fiziksel uzaklık toleransı
)

# Sonuçları göster
cv2.imshow("Bilateral Blur", bilateral)
cv2.imshow("Original", image)
cv2.imshow("Median Blur (5)", median)
cv2.waitKey(0)
cv2.destroyAllWindows()

