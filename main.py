from turtle import circle
import cv2

#reading the image, resizing and changing the color
img = cv2.imread('Images/index.jpg',1)
resized_img = cv2.resize(img, (600,400), interpolation=cv2.INTER_LINEAR,)
cv2.imshow('Original Images', resized_img)
cv2.waitKey(0)
if img is None:
    print('Could not read image')

    
#annotating with just a line
imageline = resized_img.copy()
pointA=(150,80)
pointB=(300,80)
cv2.line(imageline, pointA,pointB, (255,255,0),thickness=3)
cv2.imshow('Image Line', imageline)
cv2.waitKey(0)

#annotating with a circle
imageCircle = resized_img.copy()
circle=(240,100)
radius = 70
cv2.circle(imageCircle, circle, radius, (255,0,0), thickness=3,lineType=cv2.LINE_AA)
cv2.imshow("Image Circle", imageCircle)
cv2.waitKey(0)


#annotating with a rectangle 
imagerec = resized_img.copy()
point1 = (150,50)
point2 = (300,180)
cv2.rectangle(imagerec,point1, point2, (0,255,0), thickness=3)
cv2.imshow("Image rectangle", imagerec)
cv2.waitKey(0)