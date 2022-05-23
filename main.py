import sys
import cv2  #opencv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
image = sys.argv[1]
img = cv2.imread(image)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
var1 = pytesseract.image_to_string(img, lang='chi_tra_vert')
print(var1)

### Detecting Words
hImg,wImg,_ = img.shape
# myconfig = r'--psm 11 --oem 3'  #psm - page segmentation mode, oem - OCR engine mode
boxes = pytesseract.image_to_data(img)
print(boxes)
for x, b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0,255,0), 2)
            cv2.putText(img, b[11], (x, y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
print(boxes)

cv2.imshow('Result', img)
cv2.waitKey(0)




