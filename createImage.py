import cv2

img = cv2.imread('abba.png',0)  #0 in gray scale
# 1 0 1  
cv2.imwrite('abba_copy.png', img)