import cv2

img=cv2.imread('assests/photo.jpeg', 1)
img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)


cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()