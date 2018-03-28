import cv2
#import opencv as cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

flag = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()

    if flag: frame = cv2.Canny(frame, 100, 200)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    if cv2.waitKey(33) == ord('a'):
        print('a pressed')
        flag = not flag

cv2.destroyWindow("preview")
