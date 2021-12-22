from PIL import Image, ImageOps
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# image = Image.open("./yuheng.jpg")
# gray_image = ImageOps.grayscale(image)
# gray_image.show()

img = cv2.imread("./handwritten_1.jpeg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hImg, wImg, _ = img.shape
print(_)
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split()
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    # cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 255, 0), 1)
    # cv2.rectangle(img, (x, hImg - y), (w, h), (0, 255, 0), 1)

    # cropped_img = img[y:hImg-y, x:hImg-h]
    # cv2.imshow("cropped", cropped_img)
    # cv2.waitKey(0)

    print([[x, y, w, h, hImg, wImg], [x, hImg-y, w, hImg-h]])

    # img1 = Image.open("./handwritten_1.jpeg")
    # box = (10, 10, 10, 10)
    # region = img1.crop(box)
    # region.show()
    # cv2.putText(img, b[0], (x, hImg - y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

cv2.imshow("Image", img)
cv2.waitKey();  