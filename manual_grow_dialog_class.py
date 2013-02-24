from PyQt4.QtGui import *

class ManualGrowDialog(QDialog):
    """this class provides a dialog window to ask for light and water values"""

    def __init__(self):
        super().__init__()

        self.water_line_edit = QLineEdit()
        self.light_line_edit = QLineEdit()

        self.water_line_edit.setPlaceholderText("Water Value")
        self.light_line_edit.setPlaceholderText("Light Value")

        self.water_line_edit.clearFocus()

        self.submit_button = QPushButton("Enter Values")

        self.dialog_layout = QVBoxLayout()
        self.dialog_layout.addWidget(self.light_line_edit)
        self.dialog_layout.addWidget(self.water_line_edit)
        self.dialog_layout.addWidget(self.submit_button)

        self.setLayout(self.dialog_layout)

        #connections
        self.submit_button.clicked.connect(self.close)

    def values(self):
        return int(self.light_line_edit.text()), int(self.water_line_edit.text())