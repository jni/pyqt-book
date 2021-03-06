from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
import sys


def make_printer(num):
    def print_value():
        print(num)
    return print_value


def print_button_state(signal):
    signal_text = 'on' if signal else 'off'
    print('Button is now ' + signal_text)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QHBoxLayout()
        for i in range(5):
            button = QPushButton(' %i ' % i)
            button.pressed.connect(make_printer(i))
            layout.addWidget(button)
        self.setWindowTitle("My Awesome Window")
        singleton_widget = QWidget()
        singleton_widget.setLayout(layout)
        self.setCentralWidget(singleton_widget)

        toolbar = QToolBar('Main toolbar')
        self.addToolBar(toolbar)

        button_action = QAction('Button', self)
        button_action.setStatusTip('Your button')
        button_action.triggered.connect(print_button_state)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

    def contextMenuEvent(self, event):
        print('Context menu event happened!')

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
