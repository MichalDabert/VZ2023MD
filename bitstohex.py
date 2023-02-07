import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QHBoxLayout, QLabel, QVBoxLayout, QWidget



def bits_to_hex(b1, b2, b3, b4, b5, b6, b7, b8):
    bits = [1 if b else 0 for b in [b1, b2, b3, b4, b5, b6, b7, b8]]  # list comprehension
    decimal = int(''.join(map(str, bits)), 2)
    return hex(decimal)


class CheckboxWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.checkboxes = []
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.create_checkboxes()
        self.create_layout()

    def create_checkboxes(self):
        for i in range(8):
            checkbox = QCheckBox("bit{}".format(i+1))
            checkbox.stateChanged.connect(self.update_label)
            self.checkboxes.append(checkbox)

    def create_layout(self):
        main_layout = QVBoxLayout()
        bit_layout = QHBoxLayout()
        for checkbox in self.checkboxes:
            bit_layout.addWidget(checkbox)
        main_layout.addLayout(bit_layout)
        main_layout.addWidget(self.label)
        self.setLayout(main_layout)

    def update_label(self):
        b1, b2, b3, b4, b5, b6, b7, b8 = [checkbox.isChecked() for checkbox in self.checkboxes]
        hex_value = bits_to_hex(b1, b2, b3, b4, b5, b6, b7, b8)
        self.label.setText(hex_value)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.checkboxes[0].setChecked(not self.checkboxes[0].isChecked())
        elif event.key() == Qt.Key_2:
            self.checkboxes[1].setChecked(not self.checkboxes[1].isChecked())
        elif event.key() == Qt.Key_3:
            self.checkboxes[2].setChecked(not self.checkboxes[2].isChecked())
        elif event.key() == Qt.Key_4:
            self.checkboxes[3].setChecked(not self.checkboxes[3].isChecked())
        elif event.key() == Qt.Key_5:
            self.checkboxes[4].setChecked(not self.checkboxes[4].isChecked())
        elif event.key() == Qt.Key_6:
            self.checkboxes[5].setChecked(not self.checkboxes[5].isChecked())
        elif event.key() == Qt.Key_7:
            self.checkboxes[6].setChecked(not self.checkboxes[6].isChecked())
        elif event.key() == Qt.Key_8:
            self.checkboxes[7].setChecked(not self.checkboxes[7].isChecked())
        elif event.key() == Qt.Key_Escape:
            for checkbox in self.checkboxes:
                checkbox.setChecked(False)
        self.update_label()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CheckboxWidget()
    widget.setWindowTitle("Bits to Hex")
    widget.show()
    sys.exit(app.exec())
