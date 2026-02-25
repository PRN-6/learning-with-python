import cv2


#print(cv2.__version__)

# img = cv2.imread('1.jpg')  #read image
# cv2.imshow('image', img)  #show image
# cv2.waitKey(0)  #wait until key is pressed
# cv2.destroyAllWindows()  #destroy all windows

# cap = cv2.VideoCapture(0)  # 0 = default camera

# while True:
#     ret, frame = cap.read()
#     cv2.imshow("webcam", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor

class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        # Remove window borders
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )

        # Transparent background
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Full screen
        self.showFullScreen()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor(255, 0, 0), 5)
        painter.setPen(pen)

        # Draw sample circle in center
        center_x = self.width() // 2
        center_y = self.height() // 2
        painter.drawEllipse(center_x - 50, center_y - 50, 100, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = Overlay()
    overlay.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
