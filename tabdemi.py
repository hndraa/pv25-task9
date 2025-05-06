from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QLineEdit, QFormLayout, QInputDialog
)
from PyQt5.QtCore import Qt
import sys

class FormDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form dengan Dialog Input per Field")
        self.resize(350, 200)

        layout = QFormLayout()

        # Input tidak bisa diketik langsung (read-only)
        self.nama_input = QLineEdit()
        self.nama_input.setReadOnly(True)
        self.nama_input.setPlaceholderText("Klik untuk isi nama")
        self.nama_input.mousePressEvent = self.edit_nama

        self.nim_input = QLineEdit()
        self.nim_input.setReadOnly(True)
        self.nim_input.setPlaceholderText("Klik untuk isi NIM")
        self.nim_input.mousePressEvent = self.edit_nim

        self.bahasa_input = QLineEdit()
        self.bahasa_input.setReadOnly(True)
        self.bahasa_input.setPlaceholderText("Klik untuk pilih bahasa")
        self.bahasa_input.mousePressEvent = self.edit_bahasa

        layout.addRow("Nama:", self.nama_input)
        layout.addRow("NIM:", self.nim_input)
        layout.addRow("Bahasa Favorit:", self.bahasa_input)

        self.submit_btn = QPushButton("Submit")
        self.submit_btn.clicked.connect(self.show_result)

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addWidget(self.submit_btn)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def edit_nama(self, event):
        text, ok = QInputDialog.getText(self, "Input Nama", "Masukkan nama:")
        if ok and text.strip():
            self.nama_input.setText(text)

    def edit_nim(self, event):
        text, ok = QInputDialog.getText(self, "Input NIM", "Masukkan NIM:")
        if ok and text.strip():
            self.nim_input.setText(text)

    def edit_bahasa(self, event):
        items = ["Python", "Java", "C++", "JavaScript", "Go"]
        item, ok = QInputDialog.getItem(self, "Pilih Bahasa", "Bahasa Favorit:", items, 0, False)
        if ok and item:
            self.bahasa_input.setText(item)

    def show_result(self):
        nama = self.nama_input.text()
        nim = self.nim_input.text()
        bahasa = self.bahasa_input.text()
        if nama and nim and bahasa:
            self.result_label.setText(f"Nama: {nama}\nNIM: {nim}\nBahasa: {bahasa}")
        else:
            self.result_label.setText("Silakan lengkapi semua form!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormDialogDemo()
    window.show()
    sys.exit(app.exec_())
