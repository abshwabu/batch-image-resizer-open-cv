import cv2

import glob


images = glob.glob('*.jpg')

for image in images:
    img=cv2.imread(image,0)
    rs=cv2.resize(img,(100,100))
    cv2.imshow('images/',rs)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    cv2.imwrite('resized'+image,rs)
    