from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class form_roles(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = QFile("form_roles.ui"); f.open(QFile.ReadOnly)
        self.form = QUiLoader().load(f, self); f.close()
        self.crud = my_cruddb()
        self.form.btnSimpan.clicked.connect(self.doSimpan)
        self.form.btnUbah.clicked.connect(self.doUbah)
        self.form.btnHapus.clicked.connect(self.doHapus)
        self.form.btnBersih.clicked.connect(self.doBersih)
        self.form.table.cellClicked.connect(self.klikTabel)
        self.form.editCari.textChanged.connect(self.doCari)
        self.tampilData()

    def doBersih(self):
        f=self.form; f.edit_id.clear(); f.edit_nama_role.clear(); f.edit_keterangan.clear(); f.edit_id.setFocus()

    def doSimpan(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","id belum diisi"); return
        self.crud.simpanRole(f.edit_id.text(), f.edit_nama_role.text(), f.edit_keterangan.text())
        self.tampilData(); QMessageBox.information(self,"Info","Tersimpan"); self.doBersih()

    def doUbah(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","Pilih data dulu"); return
        self.crud.ubahRole(f.edit_id.text(), f.edit_nama_role.text(), f.edit_keterangan.text())
        self.tampilData(); QMessageBox.information(self,"Info","Diubah")

    def doHapus(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","Pilih data dulu"); return
        if QMessageBox.question(self,"Konfirmasi","Hapus data ini?",QMessageBox.Yes|QMessageBox.No)==QMessageBox.No: return
        self.crud.hapusRole(f.edit_id.text()); self.tampilData(); self.doBersih()

    def tampilData(self):
        data=self.crud.dataRole(); t=self.form.table; t.setRowCount(0)
        for row in data:
            i=t.rowCount(); t.insertRow(i)
            t.setItem(i,0,QTableWidgetItem(str(row.get("id",""))))
            t.setItem(i,1,QTableWidgetItem(str(row.get("nama_role",""))))
            t.setItem(i,2,QTableWidgetItem(str(row.get("keterangan",""))))

    def doCari(self):
        key=self.form.editCari.text(); data=self.crud.cariRole(key); t=self.form.table; t.setRowCount(0)
        for row in data:
            i=t.rowCount(); t.insertRow(i)
            t.setItem(i,0,QTableWidgetItem(str(row.get("id",""))))
            t.setItem(i,1,QTableWidgetItem(str(row.get("nama_role",""))))
            t.setItem(i,2,QTableWidgetItem(str(row.get("keterangan",""))))

    def klikTabel(self, r, c):
        t=self.form.table; f=self.form
        f.edit_id.setText(t.item(r,0).text() if t.item(r,0) else "")
        f.edit_nama_role.setText(t.item(r,1).text() if t.item(r,1) else "")
        f.edit_keterangan.setText(t.item(r,2).text() if t.item(r,2) else "")
