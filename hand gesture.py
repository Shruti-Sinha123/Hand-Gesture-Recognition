import cv2
import numpy as np

hand = cv2.imread('hand-sample.jpg',0)

ret, the = cv2.threshold(hand, 70, 255, cv2.THRESH_BINARY)

result = cv2.findContours(the.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours, hierarchy = result if len(result) == 2 else result[1:3]

hull = [cv2.convexHull(c) for c in contours]

final = cv2.drawContours(hand, hull, -1, (255,0,0))



cv2.imshow('Original Image',hand)
cv2.imshow('Thresh', the)
cv2.imshow('Convex Hull',final)

cv2.waitKey(0)
cv2.destroyAllWindows()
