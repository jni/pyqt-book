from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome Window")
        label = QLabel("Awesome stuff.")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.

app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop.
app.exec_()


# Your application won't reach here until you exit and the event 
# loop has stopped.
