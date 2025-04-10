import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


cap = cv2.VideoCapture(0)

while True:
	_,img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	
	for (x, y, m, v) in faces:
		cv2.rectangle(img, (x, y), (x+m, y+v), (255,0, 0), 2)

	cv2.imshow('Rostros Detectados', img)
	k = cv2.waitKey(30)
	if k ==27:
		break

cap.release()