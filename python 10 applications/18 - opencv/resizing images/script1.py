import cv2

zoom = .7

img = cv2.imread("spain.jpg", 1)
print(img.shape)
resized_image = cv2.resize(img, (int(img.shape[1] * zoom), int(img.shape[0] * zoom)))
print(resized_image.shape)
cv2.imshow("spain", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("spain_resized.jpeg", resized_image)