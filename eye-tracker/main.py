import cv2


#print(cv2.__version__)

# img = cv2.imread('1.jpg')  #read image
# cv2.imshow('image', img)  #show image
# cv2.waitKey(0)  #wait until key is pressed
# cv2.destroyAllWindows()  #destroy all windows

cap = cv2.VideoCapture(0)  # 0 = default camera

while True:
    ret, frame = cap.read()
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
