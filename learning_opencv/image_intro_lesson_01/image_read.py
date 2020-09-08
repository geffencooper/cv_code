# import the necessary packages
import imutils
import cv2

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("jp.png")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
roi = image[20:130, 240:350]

resized = cv2.resize(image, (200,200))

r = 300.0/w # ratio of new width to old width
dim = (300, int(h*r)) # multiply ratio by old height

resized = cv2.resize(image, dim)

resized = imutils.resize(image, width=300)

center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))

cv2.imshow("resized", rotated)
cv2.waitKey(0)