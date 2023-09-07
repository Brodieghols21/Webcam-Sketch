import cv2
import numpy as np

def sketch(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  blurred = cv2.GaussianBlur(gray, (5, 5), 0)
  edges = cv2.Canny(blurred, 50, 150)
  return edges

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  sketch_frame = sketch(frame)

  cv2.imshow("Webcam Sketch", sketch_frame)

  if cv2.waitKey(1) == 27:
    break

cap.release()
cv2.destroyAllWindows()
