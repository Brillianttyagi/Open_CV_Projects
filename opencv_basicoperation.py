import cv2

img = cv2.imread('lena.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

pic = img[316:352, 256:282]
img[15:51, 15:41] = pic

b,g,r = cv2.split(img)

cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()