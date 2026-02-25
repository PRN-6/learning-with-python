import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("leo window")
window.resize(400, 300)
window.show()

sys.exit(app.exec())




def main():
    print("Hello from window-layout!")


if __name__ == "__main__":
    main()
