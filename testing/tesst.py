import cv2
import face_recognition

img = cv2.imread("download.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
image_encode = face_recognition.face_encodings(rgb_img)[0]



cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()