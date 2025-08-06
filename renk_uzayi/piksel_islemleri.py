import cv2
img = cv2.imread("resimler/manzara1.jpg")
img_with_red = img.copy()
img_with_red[100:200, 100:200] = [0, 0, 255] # 100-200 arası kutucuğu tamamen kırmızı yapar

resized = cv2.resize(img, dsize=None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
height, width = img.shape[:2]
center = (width/2, height/2)
 
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)
 
rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))

#görüntü üzerindeki kordinatlar
x1 = 180
y1 = 60
x2 = 300
y2 = 150

cut = imgcut = img[y1:y2, x1:x2]  
# görüntü üzerinde kesilecek dörtgenin sol üst köşesinin ve
                            # sağ alt köşesinin kordinatları

im_v = cv2.vconcat([img, img])

# show the output image
cv2.imshow("Birlestirme", im_v)
cv2.imshow("Kirpma", cut)
cv2.imshow("Orijinal", img)
cv2.imshow("Buyutulmus", resized)
cv2.imshow('resimler/manzara1.jpg ', img)# ekrana basıyoruz görüntüyü
cv2.imshow('piksel manipilasyonu ', img_with_red)
cv2.imshow("Dondurulmus", rotated_image)  
cv2.waitKey(0)
cv2.destroyAllWindows()