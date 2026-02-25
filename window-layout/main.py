# import sys
# from PyQt6.QtWidgets import QApplication, QWidget ,QPushButton , QVBoxLayout

# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle("leo window")

# layout = QVBoxLayout()

# button = QPushButton("click me")
# layout.addWidget(button)

# window.setLayout(layout)
# window.show()

# def say_hello():
#     print("Hello")


# button.clicked.connect(say_hello)

# sys.exit(app.exec())

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QPainter, QColor


# class Overlay(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Remove border + Always on top + Hide from taskbar
#         self.setWindowFlags(
#             Qt.WindowType.FramelessWindowHint |
#             Qt.WindowType.WindowStaysOnTopHint |
#             Qt.WindowType.Tool
#         )

#         # Enable transparency
#         self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

#         # Make fullscreen
#         self.showFullScreen()

#     # Optional semi-transparent background
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setBrush(QColor(0, 0, 0, 100))  # Black transparent layer
#         painter.drawRect(self.rect())


# app = QApplication(sys.argv)
# overlay = Overlay()
# overlay.show()
# sys.exit(app.exec())


# def main():
#     print("Hello from window-layout!")


# if __name__ == "__main__":
#     main()

import sys
import cv2
import numpy as np

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QPainter, QColor


# -------------------------
# Worker Thread (Camera)
# -------------------------
class EyeTrackerThread(QThread):
    position_signal = pyqtSignal(int, int)

    def run(self):
        cap = cv2.VideoCapture(0)

        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        while True:
            ret, frame = cap.read()
            if not ret:
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cx = x + w // 2
                cy = y + h // 2

                # Scale to screen size (simple mapping)
                screen_x = int(cx * 2)
                screen_y = int(cy * 2)

                self.position_signal.emit(screen_x, screen_y)

        cap.release()


# -------------------------
# Overlay Window
# -------------------------
class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        self.eye_x = 0
        self.eye_y = 0

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool |
            Qt.WindowType.WindowDoesNotAcceptFocus
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        self.showFullScreen()

        # Start eye tracking thread
        self.thread = EyeTrackerThread()
        self.thread.position_signal.connect(self.update_position)
        self.thread.start()

    def update_position(self, x, y):
        self.eye_x = x
        self.eye_y = y
        self.update()  # repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 0, 0, 150))
        painter.drawEllipse(self.eye_x, self.eye_y, 40, 40)


# -------------------------
# Run App
# -------------------------
app = QApplication(sys.argv)
overlay = Overlay()
overlay.show()
sys.exit(app.exec())