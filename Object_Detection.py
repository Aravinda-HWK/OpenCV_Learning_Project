import numpy as np
import cv2

img=cv2.resize(cv2.imread('assests/soccer_practice.jpg',0),(0,0),fx=0.7,fy=0.7)
template=cv2.resize(cv2.imread('assests/shoe.png',0),(0,0),fx=0.7,fy=0.7)
h,w=template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2=img.copy()
    results=cv2.matchTemplate(img2,template,method)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(results)
    if method in [cv2.TM_SQDIFF,cv2.TM_CCOEFF_NORMED]:
        location=min_loc
    else:
        location=max_loc
    
    bottom_right=(location[0]+w,location[1]+h)
    cv2.rectangle(img2,location,bottom_right,(255,0,0),5)
    cv2.imshow('Match',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()