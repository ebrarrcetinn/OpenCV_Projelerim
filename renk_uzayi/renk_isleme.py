
import cv2


img=cv2.imread('resimler/pitbull.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_lab=cv2.cvtColor(img,cv2.COLOR_BGR2HLS_FULL)

cv2.imshow("RENKLI",img)
cv2.imshow("GRI SEVIYE",img_gray)

cv2.imshow("RENKLI",img)
cv2.imshow("RGB SEVIYE",img_rgb)

cv2.imshow("RENKLI",img)
cv2.imshow("HSV SEVIYE",img_hsv)

cv2.imshow("RENKLI",img)
cv2.imshow("LAB SEVIYE",img_lab)

cv2.waitKey(0)
cv2.destroyAllWindows()