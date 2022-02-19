# this program can help us in reading and printing the qrcode on the png file
# cv2 is used for reading from the qrcode

import qrcode
import cv2
s= "hello anshuman"
img = qrcode.make(s)
img.save("myqr1.png")

img=cv2.imread("myqr1.png")
det = cv2.QRCodeDetector()
val, pts, st_code = det.detectAndDecode(img)
print(val)
