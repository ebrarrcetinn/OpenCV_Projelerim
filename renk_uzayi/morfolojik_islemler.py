import cv2
import numpy as np
import matplotlib.pyplot as plt
 # Gri tonlama (tek kanal) 
img = cv2.imread("resimler/elma.png", 0)
img_gray = cv2.imread("resimler/elma.png", cv2.IMREAD_GRAYSCALE)

# Renkli (BGR formatında)
img_color = cv2.imread("resimler/elma.png")

  
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
  
kernel = np.ones((3, 5), np.uint8)
  
invert = cv2.bitwise_not(binr)
  
erosion = cv2.erode(invert, kernel, iterations=2)
dilation=cv2.dilate(img,kernel,iterations=3)
opening = cv2.morphologyEx(invert, cv2.MORPH_OPEN,kernel, iterations=5)
closing = cv2.morphologyEx(invert, cv2.MORPH_CLOSE,kernel, iterations=4)
tophat_gray = cv2.morphologyEx(img_gray, cv2.MORPH_TOPHAT, kernel)
tophat_color = cv2.morphologyEx(img_color, cv2.MORPH_TOPHAT, kernel)
blackhat_gray = cv2.morphologyEx(img_gray, cv2.MORPH_BLACKHAT, kernel)
blackhat_color = cv2.morphologyEx(img_color, cv2.MORPH_BLACKHAT, kernel)
gradient_color = cv2.morphologyEx(img_color, cv2.MORPH_GRADIENT, kernel)

  
cv2.imshow("original",invert)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("Orijinal Gri", img_gray)
cv2.imshow("TopHat Gri", tophat_gray)
cv2.imshow("Orijinal Renkli", img_color)
cv2.imshow("TopHat Renkli", tophat_color)
cv2.imshow("Orijinal Gri", img_gray)
cv2.imshow("BlackHat Gri", blackhat_gray)
cv2.imshow("Orijinal Renkli", img_color)
cv2.imshow("BlackHat Renkli", blackhat_color)
cv2.imshow("Sinir (Gradyan) Renkli", gradient_color)



cv2.waitKey(0)
cv2.destroyAllWindows()
