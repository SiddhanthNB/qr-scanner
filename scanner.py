import cv2
import time
import webbrowser

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
# cv2.namedWindow("test")
while True:
    _, img = cap.read()
    cv2.imshow('test-frame', img)
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        a=data
        print(str(a))
        break

cap.release()
cv2.destroyAllWindows() 