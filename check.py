import cv2
img_path = r'J:\Desktop\BIG\masks\{0A3888B5-6C49-4051-99FD-A3B48FDD9A1D}.bmp'
img = cv2.imread(img_path,cv2.IMREAD_UNCHANGED)
cv2.imshow('photo',img)
key = cv2.waitKey(0)
