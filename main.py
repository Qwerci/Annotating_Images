from turtle import circle
import cv2

img = cv2.imread('Images/index.jpg',1)
#cv2.imshow('Original Images', img)
cv2.waitKey(0)
if img is None:
    print('Could not read image')

imageline = img.copy()
resized = cv2.resize(imageline, (600,400), interpolation=cv2.INTER_LINEAR)
pointA=(150,80)
pointB=(300,80)
cv2.line(resized, pointA,pointB, (255,255,0),thickness=3)
#cv2.imshow('Image Line', resized)
cv2.waitKey(0)


imageCircle = img.copy()
resized_2 = cv2.resize(imageCircle, (600,400), interpolation=cv2.INTER_LINEAR,)
circle=(240,100)
radius = 70
cv2.circle(resized_2, circle, radius, (255,0,0), thickness=3,lineType=cv2.LINE_AA)
cv2.imshow("Image Circle", resized_2)
cv2.waitKey(0)