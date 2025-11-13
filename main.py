# main.py
import sys, os, traceback
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from form_jenis import form_jenis
from form_roles import form_roles
from form_users import form_users
from form_informasi import form_informasi
from form_produk import form_produk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class HalamanUtama(QMainWindow):
    def __init__(self):
        super().__init__()
        # pastikan main_window.ui pakai path absolut
        ui_path = os.path.join(BASE_DIR, "main.ui")
        f = QFile(ui_path);
        if not f.exists():
            QMessageBox.critical(self, "UI tidak ditemukan", f"Tidak menemukan: {ui_path}")
        f.open(QFile.ReadOnly)
        self.ui = QUiLoader().load(f, self); f.close()

        self._windows = []

        # koneksikan dengan pelindung try/except
        self.ui.actionFormJenis.triggered.connect(lambda: self.safe_open(form_jenis))
        self.ui.actionFormRoles.triggered.connect(lambda: self.safe_open(form_roles))
        self.ui.actionFormUsers.triggered.connect(lambda: self.safe_open(form_users))
        self.ui.actionFormInformasi.triggered.connect(lambda: self.safe_open(form_informasi))
        self.ui.actionFormProduk.triggered.connect(lambda: self.safe_open(form_produk))

    def safe_open(self, FormClass):
        try:
            w = FormClass()
            w.show()
            self._windows.append(w)  # jaga agar tidak di-GC
        except Exception as e:
            # tampilkan traceback agar ketahuan letak errornya
            tb = traceback.format_exc()
            QMessageBox.critical(self, "Gagal membuka form", f"{e}\n\n{tb}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = HalamanUtama()
    mw.ui.show()
    sys.exit(app.exec())
