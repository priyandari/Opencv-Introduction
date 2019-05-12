import cv2

img = cv2.imread('abba.png',0)  #0 in gray scale
# 1 0 1  

cv2.imshow('First image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()